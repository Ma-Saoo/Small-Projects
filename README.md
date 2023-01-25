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

# ProbabilitySimulations.py
## Monty-Hall Problem
(from wikipedia)
> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

Rules :
- The host must always open a door that was not picked by the contestant.
- The host must always open a door to reveal a goat and never the car.
- The host must always offer the chance to switch between the originally chosen door and the remaining closed door.

Solution: By my simulation, WIN ~ 66.66% if we switch the guess

Explanation : Say the player chooses a door which has a goat behind it. The host must then open one of the two doors remaining. As per the rules, the host CANNOT open a door that was chosen by the contestant, and a door that reveals the car. Thus, the host must open a door that reveals the goat. Now we know that our initial door guess reveals a goat and the other door that also reveals a goat, switching from our original guess to the remaining closed door will get us the car 100% of the time. In conclusion, everytime our initial door guess has a goat behind it, then, by switching, we will get the car. In addition, the probability that our initial door guess reveals a goat is 66.66%. Therefore, the probability of winning the game if we switch is 66.66% * 1 = 66.66%

## 100 Prisoners Problem
(from wikipedia)
> The director of a prison offers 100 death row prisoners, who are numbered from 1 to 100, a last chance. A room contains a cupboard with 100 drawers. The director randomly puts one prisoner's number in each closed drawer. The prisoners enter the room, one after another. Each prisoner may open and look into 50 drawers in any order. The drawers are closed again afterwards. If, during this search, every prisoner finds their number in one of the drawers, all prisoners are pardoned. If just one prisoner does not find their number, all prisoners die. Before the first prisoner enters the room, the prisoners may discuss strategy — but may not communicate once the first prisoner enters to look in the drawers. What is the prisoners' best strategy?

Solution: By my simulation, WIN ~ 31.2% if we follow the cycle strategy

Strategy : 
  1. Each prisoner first opens the drawer labeled with their own number.
  2. If this drawer contains their number, they are done and were successful.
  3. Otherwise, the drawer contains the number of another prisoner, and they next open the drawer labeled with this number.
  4. The prisoner repeats steps 2 and 3 until they find their own number, or fail because the number is not found in the first fifty opened drawers.

Explanation : If every prisoner randomly guesses the draws, then the probability of a single prisoner finding their number is 50/100 = 1/2 = 50%. It follows that the probability of 100 prisoners all getting their numbers is (1/2)<sup>100</sup> = 7.88 * 10<sup>-29</sup> %. If we follow the strategy, the prisoners always wins if the longest cycle of numbers is 50. The probability that a random permutation of cycles having at most 50 numbers in any cycle is: 1 - (1/51 + 1/52 + ... + 1/99 + 1/100) ~ 0.3118 = 31.2%

# Orbit Simulators
A simulation of what would happen to our solar system if the Sun had disappeared. The simulation was constructed based on Newton's Law of Universal Gravitation. Consequently, the simulation is an approximation as, in reality, gravity is not a force propagated between bodies but rather the effect of curved spacetime. The model consists of the Sun, Mercury, Venus, Earth, and Mars. The outer system planets are not included as they orbit too far relative to the other four, which messes up the scale.

The calculations for each planet took into account the gravitational pull of the other three planets and the Sun; however, as expected, the gravitational effects of the remaining planets are minimal relative to the Sun. Orbit Simulator V1 shows what would happen if the Sun disappeared instantaneously, whereas Orbit Simulator V2, after two seconds, has the Sun losing mass constantly until nil over fifteen seconds.
