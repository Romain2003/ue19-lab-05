import requests
import sys
import time

def get_joke():
    """Récupère une blague depuis l'API JokeAPI"""
    url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["type"] == "single":
            return data["joke"]
        else:
            return f"{data['setup']}\n{data['delivery']}"
            
    except requests.RequestException as e:
        return f"Erreur lors de la récupération de la blague: {e}"

def main():
    print("Récupération d'une blague...")
    joke = get_joke()
    print("\nVoici votre blague :")
    print("-" * 40)
    print(joke)
    print("-" * 40)

if __name__ == "__main__":
    main()
