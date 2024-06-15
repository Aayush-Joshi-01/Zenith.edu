import mongoose from 'mongoose'
// const mongoose = require('mongoose');

// MongoDB connection string (replace with your actual connection string)
const mongoURI = 'mongodb+srv://ronakchhabra:ruro1234@ronakchhabra.tvgeidk.mongodb.net/?retryWrites=true&w=majority&appName=Ronakchhabra';

// Connect to MongoDB
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', async function() {
  console.log('Connected to the database');

  // Define your updated schema
  const yourSchema = new mongoose.Schema({
    name: String,
    age: Number,
    newField: { type: String, default: 'defaultValue' } // New field added
  });

  // Initialize your model
  const YourModel = mongoose.model('YourModel', yourSchema);

  try {
    // Optionally, drop the collection if you need to recreate it (use with caution)
    // await mongoose.connection.db.dropCollection('yourmodels');

    // Update existing documents to include new fields
    const result = await YourModel.updateMany({}, { $set: { newField: 'defaultValue' } });
    console.log('Documents updated:', result);

  } catch (error) {
    console.error('Error updating documents:', error);
  }

  // Close the connection
  mongoose.connection.close();
});

// Disconnect gracefully on script termination
process.on('SIGINT', () => {
  mongoose.connection.close(() => {
    console.log('Mongoose connection disconnected due to app termination');
    process.exit(0);
  });
});
