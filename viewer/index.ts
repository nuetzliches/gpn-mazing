import express from "express";

const HOSTNAME = 'localhost'
const PORT = 3001;

const app = express();

app.use('/assets', express.static(__dirname + '/assets'));

app.get('/*', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.listen(PORT, () => {
    console.log(`Server listening on port http://${HOSTNAME}:${PORT}`);
    console.log('Press Ctrl+C to quit.');
});