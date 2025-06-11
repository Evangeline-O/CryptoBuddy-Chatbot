# CryptoBuddy Chatbot

import random

print("Hey there! I’m CryptoBuddy 🤖. Let’s explore some crypto options together!")

# Predefined crypto database
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

# Start chatbot loop
while True:
    user_query = input("\nAsk me anything about crypto (or type 'exit' to quit): ").lower()

    # Random suggestion (20% chance)
    if random.randint(1,5) == 1:
        random_coin = random.choice(list(crypto_db.keys()))
        print(f"CryptoBuddy: By the way, have you looked into {random_coin}? It's quite interesting! 😉")

    if user_query == 'exit':
        print("CryptoBuddy: Goodbye! 👋 Remember to always DYOR (Do Your Own Research)!")
        break

    elif "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print("⚠️ Disclaimer: Cryptocurrency investments are risky. Always do your own research before investing!")
        print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

    elif "profitable" in user_query:
        candidates = [coin for coin in crypto_db 
                      if crypto_db[coin]["price_trend"] == "rising" 
                      and crypto_db[coin]["market_cap"] == "high"]
        print("⚠️ Disclaimer: Cryptocurrency investments are risky. Always do your own research before investing!")
        if candidates:
            print(f"CryptoBuddy: These are highly profitable: {', '.join(candidates)} 💰")
        else:
            print("CryptoBuddy: No highly profitable coins match the criteria right now.")

    elif "trending" in user_query or "growth" in user_query:
        trending_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print("⚠️ Disclaimer: Cryptocurrency investments are risky. Always do your own research before investing!")
        print(f"CryptoBuddy: The trending coins are: {', '.join(trending_coins)} 🚀")

    else:
        print("CryptoBuddy: Hmm 🤔 I'm still learning. Try asking about 'sustainable', 'profitable', or 'trending' cryptos.")
