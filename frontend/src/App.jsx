import { useState, useRef } from 'react'
import './App.css'

function App() {
  const [text, setText] = useState('')
const [result, setResult] = useState(null)
const [loading, setLoading] = useState(false)
const [image, setImage] = useState(null)
const [language, setLanguage] = useState('')
const [extractedText, setExtractedText] = useState('')
const [mlAnalysis, setMlAnalysis] = useState(null)

const fileInputRef = useRef(null)

 const analyzeText = async () => {
  const hasText = text.trim() !== ''
  const hasImage = image !== null

  if (!hasText && !hasImage) {
    setResult({
      type: 'warning',
      title: 'No Message',
      score: 0,
      threat: 'No Message',
      reason: 'Please enter a message or select a screenshot to analyze.',
      indicators: []
    })
    return
  }

 setLoading(true)
setResult(null)
setMlAnalysis(null)

  try {
    let response

    // If text is present, ALWAYS prioritize text
    if (hasText) {
      response = await fetch(
        'https://surakshatext-backend.onrender.com/analyze',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            text: text
          })
        }
      )
    } else {
      // Only analyze image when there is no text
      const formData = new FormData()
      formData.append('file', image)

      response = await fetch(
        'https://surakshatext-backend.onrender.com/analyze-image',
        {
          method: 'POST',
          body: formData
        }
      )
    }

    if (!response.ok) {
      throw new Error('Server error')
    }

    const data = await response.json()

if (hasText) {
  setExtractedText('')
  setLanguage('')
} else {
  setExtractedText(data.extracted_text || '')
  setLanguage(data.language || '')
}

const analysis = hasText ? data : data.analysis

setMlAnalysis(analysis.ml_analysis || null)

let resultType = 'safe'

if (analysis.classification === 'DANGEROUS') {
  resultType = 'danger'
} else if (analysis.classification === 'SUSPICIOUS') {
  resultType = 'suspicious'
}

    setResult({
      type: resultType,
      title:
        analysis.classification === 'DANGEROUS'
          ? 'Dangerous Message'
          : analysis.classification === 'SUSPICIOUS'
          ? 'Suspicious Message'
          : 'Safe Message',
      score: analysis.risk_score,
      threat:
        analysis.indicators.length > 0
          ? analysis.indicators[0]
          : 'No Threat Detected',
      reason: analysis.recommendation,
      indicators: analysis.indicators
    })
  } catch (error) {
    setResult({
      type: 'warning',
      title: 'Connection Error',
      score: 0,
      threat: 'Backend Unavailable',
      reason:
        'Could not connect to the SurakshaText analysis server. Make sure the backend is running.',
      indicators: []
    })
  } finally {
    setLoading(false)
  }
}

  return (
    <div className="app">
      <header className="navbar">
        <div className="logo">
          Suraksha<span>Text</span>
        </div>

        <nav>
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="#features">Features</a>
        </nav>

        <button className="login-btn">Get Started</button>
      </header>

      <main>
        <section id="home" className="hero-section">
          <div className="hero-content">
            <p className="tagline">AI-POWERED TEXT SAFETY</p>

            <h1>
              Stay Safe.
              <br />
              <span>Stay Surakshit.</span>
            </h1>

            <p className="hero-description">
              SurakshaText helps you identify harmful, suspicious, and
              potentially dangerous messages before they become a threat.
            </p>

            <div className="hero-buttons">
              <button className="primary-btn">Analyze Text</button>
              <button className="secondary-btn">Learn More</button>
            </div>
          </div>

          <div className="hero-card">
            <div className="card-header">
              <span className="status-dot"></span>
              Text Analysis
            </div>

           <div className="message">
<textarea
  value={text}
 onChange={(e) => {
  setText(e.target.value)
  setImage(null)
  setExtractedText('')
  setLanguage('')
  setResult(null)
  setMlAnalysis(null)
}}
  placeholder="Paste or type a message here..."
/>

  <div className="image-upload">
    <label htmlFor="image-input">📷 Analyze Screenshot</label>

    <input
  ref={fileInputRef}
  id="image-input"
  type="file"
  accept="image/*"
  onChange={(e) => {
    setImage(e.target.files[0])
    setText('')
    setResult(null)
    setExtractedText('')
    setLanguage('')
    setMlAnalysis(null)
  }}
/>

    {image && (
      <p className="selected-image">
        Selected: {image.name}
      </p>
    )}
  </div>
</div>

            <button className="analyze-btn" onClick={analyzeText}>
              {loading ? 'Analyzing...' : 'Analyze Message'}
            </button>

            {result && (
              <div className={`result ${result.type}`}>
              {image && extractedText && (
  <div className="extracted-text">
    <h4>Extracted Text</h4>
    <p>{extractedText}</p>
  </div>
)}
{language && (
  <div className="detected-language">
    <span>Detected Language:</span>{' '}
    <strong>{language}</strong>
  </div>
)}
                <div className="result-top">
                  <h3>{result.title}</h3>
                  <span>{result.score}% Risk</span>
                </div>

                <div className="risk-bar">
                  <div
                    className="risk-fill"
                    style={{ width: `${result.score}%` }}
                  ></div>
                </div>

                <div className="threat-type">
                  <span>Threat Type</span>
                  <strong>{result.threat}</strong>
                </div>

                <p>{result.reason}</p>

{mlAnalysis && (
  <div className="ml-analysis">
    <h4>ML Analysis</h4>

    <div className="ml-details">
      <span>Classification:</span>
      <strong>{mlAnalysis.classification}</strong>
    </div>

    <div className="ml-details">
      <span>Confidence:</span>
      <strong>{mlAnalysis.confidence}%</strong>
    </div>
  </div>
)}

{result.indicators.length > 0 && (
                  <div className="indicators">
                    <h4>Detected Indicators</h4>

                    <div className="indicator-list">
                      {result.indicators.map((indicator, index) => (
                        <span key={index} className="indicator">
                          {indicator}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        </section>

        <section id="features" className="features-section">
          <p className="section-label">WHY SURAKSHATEXT</p>

          <h2>Protection when you need it.</h2>

          <div className="features">
            <div className="feature-card">
              <h3>🔍 Smart Detection</h3>
              <p>
                Detect suspicious and potentially harmful text using
                intelligent analysis.
              </p>
            </div>

            <div className="feature-card">
              <h3>🛡️ Stay Protected</h3>
              <p>
                Identify threats before they can cause harm or lead to unsafe
                decisions.
              </p>
            </div>

            <div className="feature-card">
              <h3>⚡ Fast Analysis</h3>
              <p>
                Get quick results so you can make safer decisions in real time.
              </p>
            </div>
          </div>
        </section>

        <section id="about" className="about-section">
          <p className="section-label">ABOUT SURAKSHATEXT</p>

          <h2>Built for a safer digital world.</h2>

          <p>
            SurakshaText is designed to make digital communication safer by
            helping users understand potentially harmful or suspicious text.
          </p>
        </section>
      </main>

      <footer>
        <p>© 2026 SurakshaText. Stay Safe. Stay Surakshit.</p>
      </footer>
    </div>
  )
}

export default App