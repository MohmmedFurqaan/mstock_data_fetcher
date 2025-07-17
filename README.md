<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<!--   <title>mStock Historical Data Fetcher Type-A</title> -->
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; color: #222;">

  <h1>📊 mStock Historical Data Fetcher type A</h1>
  <p>This Python project allows you to fetch historical stock market data from the <strong>mStock API</strong> using secure access tokens and save the data in <code>JSON</code> format.</p>

  <h2>📁 Project Structure</h2>
  <pre>
mstock_historical_data_fetcher/
├── config/
│   └── config.py               # Stores API_KEY and PRIVATE_KEY
├── data/                       # Stores fetched JSON output
├── src/
│   ├── fetch_data.py           # Main script to fetch and save data
│   └── utils/
│       └── _token.py           # Token generation logic
├── README.html                 # Project documentation (this file)
└── requirements.txt            # Python dependencies
  </pre>

  <h2>🚀 How to Use</h2>
  <ol>
    <li>Clone or download the repository.</li>
    <li>Create a <code>config.py</code> file in <code>config/</code> with the following:
      <pre><code>
API_KEY = "your_actual_api_key"
USERNAME = "your_username"
PASSWORD = "your_password"
PRIVATE_KEY = "your_private_key"
      </code></pre>
    </li>
    <li>Install required packages:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Run the script:
      <pre><code>python src/fetch_data.py</code></pre>
    </li>
  </ol>

  <h2>🔑 How to Get Access Token</h2>
  <ol>
    <li>Log into your <strong>mStock</strong> account via browser or app.</li>
    <li>Use registered credentials to obtain access token via the token API (handled in <code>_token.py</code>).</li>
    <li>You <strong>must register your mobile number</strong> with the mStock API to use it correctly.</li>
  </ol>

  <h2>📤 Output Formats</h2>
  <ul>
    <li><strong>JSON Format:</strong> All fetched historical data is stored as structured JSON files in the <code>data/</code> folder.</li>
    <li>File naming format: <code>&lt;symbol&gt;_&lt;range&gt;_&lt;interval&gt;.json</code></li>
  </ul>

  <h2>🔄 Example Output File</h2>
  <p>For symbol <code>TCS</code>, interval <code>1d</code>, and range <code>1mo</code>:</p>
  <pre>data/TCS_1mo_1d.json</pre>

  <h2>🛠 Features</h2>
  <ul>
    <li>Authenticated token-based API access</li>
    <li>Parameter flexibility: symbol, interval, and range</li>
    <li>Data saved in JSON for easy processing or analysis</li>
    <li>Error handling for failed requests and missing tokens</li>
  </ul>

  <h2>📦 Dependencies</h2>
  <pre><code>requests
</code></pre>


  <h2>📞 Contact</h2>
  <p>For support, please reach out to your mStock API provider for API key/token issues.</p>

</body>
</html>
