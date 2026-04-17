from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db.database import execute_query

router = APIRouter()

class DepositRequest(BaseModel):
    account_id: int
    amount: float

class WithdrawRequest(BaseModel):
    account_id: int
    amount: float

class TransferRequest(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float

# GET /transactions/:account_id - get transaction history
@router.get("/{account_id}")
def get_transactions(account_id: int):
    try:
        rows = execute_query(
            "SELECT * FROM transactions WHERE account_id = $1 ORDER BY created_at DESC",
            (account_id,)
        )
        if not rows:
            raise HTTPException(status_code=404, detail="No transactions found")
        return {"account_id": account_id, "transactions": rows}
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

# POST /transactions/deposit
@router.post("/deposit")
def deposit(req: DepositRequest):
    try:
        if req.amount <= 0:
            raise HTTPException(status_code=400, detail="Amount must be positive")

        execute_query(
            "UPDATE accounts SET balance = balance + %s WHERE id = %s",
            (req.amount, req.account_id)
        )
        execute_query(
            "INSERT INTO transactions (account_id, type, amount) VALUES (%s, 'deposit', %s)",
            (req.account_id, req.amount)
        )
        return {"message": "Deposit successful", "account_id": req.account_id, "amount": req.amount}
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

# POST /transactions/withdraw
@router.post("/withdraw")
def withdraw(req: WithdrawRequest):
    try:
        if req.amount <= 0:
            raise HTTPException(status_code=400, detail="Amount must be positive")

        rows = execute_query(
            "SELECT balance FROM accounts WHERE id = %s",
            (req.account_id,)
        )
        if not rows:
            raise HTTPException(status_code=404, detail="Account not found")

        balance = rows[0][0]
        if balance < req.amount:
            raise HTTPException(status_code=400, detail="Insufficient funds")

        execute_query(
            "UPDATE accounts SET balance = balance - %s WHERE id = %s",
            (req.amount, req.account_id)
        )
        execute_query(
            "INSERT INTO transactions (account_id, type, amount) VALUES (%s, 'withdrawal', %s)",
            (req.account_id, req.amount)
        )
        return {"message": "Withdrawal successful", "account_id": req.account_id, "amount": req.amount}
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

# POST /transactions/transfer
@router.post("/transfer")
def transfer(req: TransferRequest):
    try:
        if req.amount <= 0:
            raise HTTPException(status_code=400, detail="Amount must be positive")

        rows = execute_query(
            "SELECT balance FROM accounts WHERE id = %s",
            (req.from_account_id,)
        )
        if not rows:
            raise HTTPException(status_code=404, detail="Source account not found")

        balance = rows[0][0]
        if balance < req.amount:
            raise HTTPException(status_code=400, detail="Insufficient funds")

        execute_query(
            "UPDATE accounts SET balance = balance - %s WHERE id = %s",
            (req.amount, req.from_account_id)
        )
        execute_query(
            "UPDATE accounts SET balance = balance + %s WHERE id = %s",
            (req.amount, req.to_account_id)
        )
        execute_query(
            "INSERT INTO transactions (account_id, type, amount) VALUES (%s, 'transfer_out', %s)",
            (req.from_account_id, req.amount)
        )
        execute_query(
            "INSERT INTO transactions (account_id, type, amount) VALUES (%s, 'transfer_in', %s)",
            (req.to_account_id, req.amount)
        )
        return {"message": "Transfer successful", "from": req.from_account_id, "to": req.to_account_id, "amount": req.amount}
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")