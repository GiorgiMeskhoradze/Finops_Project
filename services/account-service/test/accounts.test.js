const request = require('supertest');
const app = require('../src/app');

// mock the db so tests don't need a real database
jest.mock('../src/db', () => ({
    query: jest.fn(),
}));

const db = require('../src/db');

describe('Account Service', () => {

    afterEach(() => {
        jest.clearAllMocks();
    });

    describe('GET /health', () => {
        it('should return 200 and status ok', async () => {
            const res = await request(app).get('/health');
            expect(res.statusCode).toBe(200);
            expect(res.body.status).toBe('ok');
        });
    });

    describe('GET /accounts/:id', () => {
        it('should return account when found', async () => {
            db.query.mockResolvedValueOnce({
                rows: [{ id: 1, owner_name: 'John Doe', balance: 1000 }],
            });

            const res = await request(app).get('/accounts/1');
            expect(res.statusCode).toBe(200);
            expect(res.body.owner_name).toBe('John Doe');
        });

        it('should return 404 when account not found', async () => {
            db.query.mockResolvedValueOnce({ rows: [] });

            const res = await request(app).get('/accounts/99');
            expect(res.statusCode).toBe(404);
        });
    });

    describe('POST /accounts', () => {
        it('should create account and return 201', async () => {
            db.query.mockResolvedValueOnce({
                rows: [{ id: 1, owner_name: 'Jane Doe', balance: 500 }],
            });

            const res = await request(app)
                .post('/accounts')
                .send({ owner_name: 'Jane Doe', initial_balance: 500 });

            expect(res.statusCode).toBe(201);
            expect(res.body.owner_name).toBe('Jane Doe');
        });

        it('should return 400 if owner_name is missing', async () => {
            const res = await request(app)
                .post('/accounts')
                .send({});

            expect(res.statusCode).toBe(400);
        });
    });

});
