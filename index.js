const { onRequest } = require("firebase-functions/v2/https");
const logger = require("firebase-functions/logger");
const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();

// CORS middleware setup
const cors = require('cors')({ origin: true });

exports.analyzeText = functions.https.onRequest((req, res) => {
  cors(req, res, () => {
    // Ensure the request method is POST
    if (req.method !== 'POST') {
      return res.status(405).json({ error: 'Method Not Allowed' });
    }

    // Proceed with the sentiment analysis
    const textToAnalyze = req.body.text || "";
    const natural = require("natural");
    const Analyzer = natural.SentimentAnalyzer;
    const stemmer = natural.PorterStemmer;
    const analyzer = new Analyzer("English", stemmer, "afinn");

    // Analyze the sentiment of the text
    const sentiment = analyzer.getSentiment(textToAnalyze.split(' '));
    res.json({ sentiment: sentiment });
  });
});
