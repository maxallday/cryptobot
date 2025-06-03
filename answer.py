# Import required libraries
import requests  # Allows fetching real-time crypto data from an API
import nltk
nltk.download('punkt_tab') # NLP library for processing user input
from nltk.tokenize import word_tokenize  # Tokenizes user input into words



# ----------------------------- #
# 📌 STEP 1: Define the Crypto Database
# ----------------------------- #
# This dictionary stores key data about different cryptocurrencies.
# Each coin has attributes such as market cap, energy use, sustainability score, use case, risk level, and community sentiment.
crypto_db = {  
    "bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "very high",  
        "energy_use": "high",  
        "sustainability_score": 3,  
        "use_case": "Digital Gold, Store of Value",  
        "risk_level": "Medium",  
        "community_sentiment": "Strong"  
    },  
    "ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6,  
        "use_case": "Smart Contracts, DApps",  
        "risk_level": "Medium",  
        "community_sentiment": "Strong"  
    },  
    "cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8,  
        "use_case": "Scalable Blockchain, Eco-Friendly",  
        "risk_level": "Low",  
        "community_sentiment": "Positive"  
    },  
    "solana": {  
        "price_trend": "rising",  
        "market_cap": "medium-high",  
        "energy_use": "low",  
        "sustainability_score": 7,  
        "use_case": "High-Speed Transactions, NFTs",  
        "risk_level": "Medium",  
        "community_sentiment": "Growing"  
    },  
    "polkadot": {  
        "price_trend": "stable",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 7,  
        "use_case": "Cross-Chain Interoperability",  
        "risk_level": "Medium",  
        "community_sentiment": "Positive"  
    },  
    "avalanche": {  
        "price_trend": "rising",  
        "market_cap": "medium-low",  
        "energy_use": "low",  
        "sustainability_score": 6,  
        "use_case": "Fast Transactions, Smart Contracts",  
        "risk_level": "High",  
        "community_sentiment": "Mixed"  
    }  
}

# ----------------------------- #
# 📌 STEP 2: Fetch Real-Time Crypto Prices using CoinGecko API
# ----------------------------- #
# This function calls the CoinGecko API to retrieve the latest cryptocurrency price.
def get_crypto_price(crypto_name):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=usd"  # API request URL
    response = requests.get(url).json()  # Sends request and parses JSON response
    
    # Check if the crypto name exists in the API response
    if crypto_name in response:
        return f"{crypto_name.capitalize()} is currently priced at ${response[crypto_name]['usd']} USD."
    
    return "Sorry, I couldn't fetch real-time data for that coin."

# ----------------------------- #
# 📌 STEP 3: Process User Queries using NLP (Natural Language Processing)
# ----------------------------- #
# This function analyzes the user input and provides appropriate recommendations based on keywords.
def process_query(user_query):
    tokens = word_tokenize(user_query.lower())  # Convert input to lowercase and tokenize words
    
    # If user asks for the price of a crypto
    if "price" in tokens:
        crypto_name = next((coin for coin in crypto_db if coin in tokens), None)
        return get_crypto_price(crypto_name) if crypto_name else "Please specify a crypto name for pricing."
    
    # If user asks for the most sustainable crypto
    elif "sustainable" in tokens:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend.capitalize()}! 🌱 It’s one of the most sustainable options available."
    
    # If user asks for a crypto with strong growth potential
    elif "growth" in tokens:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["market_cap"])
        return f"For long-term growth, consider {recommend.capitalize()}! 📈 It has a strong market cap."
    
    # If user asks for energy consumption of a specific crypto
    elif "energy" in tokens or "consumption" in tokens:
        crypto_name = next((coin for coin in crypto_db if coin in tokens), None)
        return f"{crypto_name.capitalize()} consumes {crypto_db[crypto_name]['energy_use']} energy." if crypto_name else "Please specify a crypto name to check energy consumption." 
    
    # risk level of a specific crypto
    elif "risk" in tokens:
        recommend  = max(crypto_db,key=lambda x:crypto_db[x]["risk_level"])
        return f"For lower risk consider {recommend.capitalize()}! ,It has significantly lower risk levels"
    
    # If user wants community sentiment about a specific crypto
    elif "community" in tokens:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["community_sentiment"])
        return f"{recommend.capitalize()} has a strong community sentiment! 🤝 It’s well-supported by its users."
    
    # If user asks for the purpose/use case of a crypto 
    elif "use case" in tokens or "purpose" in tokens:
        crypto_name = next((coin for coin in crypto_db if coin in tokens), None)
        return f"{crypto_name.capitalize()} is used for {crypto_db[crypto_name]['use_case']}." if crypto_name else "Please specify a crypto name for its purpose."
    
    # Default response if user input doesn’t match any category
    return "I can help with trends, sustainability, risk assessment, and community insights! Ask me something crypto-related."

# ----------------------------- #
# 📌 STEP 4: Chatbot Conversation Loop
# ----------------------------- #
# This section starts the chatbot and continuously takes user input until they choose to exit.
print("\n🚨 Disclaimer: Crypto investments carry risks—always do your own research! 🚨\n")
print("Welcome to CryptoMax! Type your question about cryptocurrency or type 'exit' to quit.")

while True:
    user_input = input("\nYou: ")  # Get user input
    
    # If user types 'exit' or 'quit', end the chatbot session
    if user_input.lower() in ["exit", "quit","bye","Kwaheri","baadae","see ya","arios","stop",'enough']:
        print("\nCryptoMax: Goodbye! Stay informed and invest wisely. 🚀\n")
        break
    
    # Process the user's query and provide a response
    response = process_query(user_input)
    print(f"CryptoBuddy: {response}")
