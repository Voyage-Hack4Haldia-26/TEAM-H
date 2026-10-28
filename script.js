try { require("dotenv").config(); } catch (e) {}
const express = require("express");
const cors = require("cors");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/", (req, res) => res.sendFile(path.join(__dirname, "index.html")));

app.get("/health", (req, res) =>
  res.json({ status: "ok", project: "Team H: Live Canteen Order Tracker", stack: "node" })
);

app.post("/api/orders", (req, res) => {
  // TODO: Place an order
  res.status(501).json({ error: "Not implemented", todo: "Place an order" });
});

app.patch("/api/orders/:id", (req, res) => {
  // TODO: Move to the next status
  res.status(501).json({ error: "Not implemented", todo: "Move to the next status" });
});

app.get("/api/orders/stream", (req, res) => {
  // TODO: SSE stream of order updates
  res.status(501).json({ error: "Not implemented", todo: "SSE stream of order updates" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Team H server running on http://localhost:${PORT}`));
