require('dotenv').config();
const express = require('express');
const accountRoutes = require('./routes/accounts');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'ok', service: 'account-service' });
});

app.use('/accounts', accountRoutes);

app.listen(PORT, () => {
    console.log(`account-service running on port ${PORT}`);
});

module.exports = app;