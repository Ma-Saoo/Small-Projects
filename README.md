# Blackjack.py
Information:
- Play a game of blackjack against a computer
- Typical deck of 52 cards, though with no suits
- There are 4 cards of each rank
- When a card is drawn from the deck, that card is removed from the list to ensure probabilities are correct (although the difference is insignificant)
- Sort-of-smart AI who follows the algorithm :
  1. If hand is lower than or equal to 16, hit
  2. If hand is higher than or equal to 18, stand
  3. If hand is a soft 17 (A 17 from a 6, and an 11 from an Ace), hit
  4. If hand is a hard 17 (A 17 without aces), stand
- Used time.sleep(0.5) many times as, without it, its too fast and harsh for the eyes
- Codes are segmented into sections with comments explaining what they do
- Will be made more efficient in the future
