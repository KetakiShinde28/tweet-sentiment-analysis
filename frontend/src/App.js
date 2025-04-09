import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [sentiment, setSentiment] = useState(null);

  const handleSubmit = async () => {
    if (!text.trim()) return;
    try {
      const response = await axios.post('http://localhost:5000/predict', { text });
      const result = response.data.sentiment;
      setSentiment(result); // Directly use the emotion label (e.g., joy, sadness)
    } catch (error) {
      console.error('Error:', error);
      setSentiment('Error predicting sentiment');
    }
  };

  const emojiMap = {
    joy: '😊',
    sadness: '😢',
    anger: '😠',
    fear: '😨',
    love: '❤️',
    surprise: '😲'
  };
  
  return (
    <div className="container">
      <h1>Tweet Vibe Checker 💬</h1>
      <textarea
        placeholder="Type or paste a tweet..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      ></textarea>
      <button onClick={handleSubmit}>Analyze Emotion</button>

      {sentiment && (
        <div className={`result ${sentiment.toLowerCase()}`}>
        Emotion: <span>{emojiMap[sentiment] || ''} {sentiment}</span>
      </div>      
      )}
    </div>
  );
}

export default App;
