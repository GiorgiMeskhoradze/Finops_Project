const express = require('express');
const router = express.Router();
const db = require('../db');

// GET /accounts/:id - get account by id
router.get('/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const result = await db.query('SELECT * FROM accounts WHERE id = $1', [id]);

        if (result.rows.length === 0) {
            return res.status(404).json({ error: 'Account not found' });
        }

        res.json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// POST /accounts - create new account
router.post('/', async (req, res) => {
    try {
        const { owner_name, initial_balance } = req.body;

        if (!owner_name) {
            return res.status(400).json({ error: 'owner_name is required' });
        }

        const result = await db.query(
            'INSERT INTO accounts (owner_name, balance) VALUES ($1, $2) RETURNING *',
            [owner_name, initial_balance || 0]
        );

        res.status(201).json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

// GET /accounts/:id/balance - get balance only
router.get('/:id/balance', async (req, res) => {
    try {
        const { id } = req.params;
        const result = await db.query('SELECT balance FROM accounts WHERE id = $1', [id]);

        if (result.rows.length === 0) {
            return res.status(404).json({ error: 'Account not found' });
        }

        res.json({ account_id: id, balance: result.rows[0].balance });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
    }
});

module.exports = router;