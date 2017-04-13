# Applidium-Challenges
This Contains solution to intro challenges for Applidium internship application

# Challenge 1 (Which Restaurant to choose?)

Assumptions:
* There are at least 7 Restaurants.
* We want to be as close as possible to the optimal value but not necessarily stick to it.
* Distinct dishes are available on distinct restaurants only.
* We will input the list until we receive an empty input with just a '\n' char.
* If faced by the choice of to have total calorie either more or less than optimal, we would select one which results in less abs distance of total calorie from optimal calories

Approach:
* Divide the optimal weekly calorie count with 7 to get the estimate daily requirement. We will call this value daily optimal.
* Divide the entire dishes list into three sorted lists. One having calorie value less the daily optimal, one equal to daily optimal and last one greater than daily optimal.
* We pick up all or maximum of 7 dishes from 2nd list having calorie value equal to daily optimal.
* If we are still left to pick up dishes, we pick them in a fashion that total weekly calorie is as close to optimal as possible. Workflow for that would be:
  * Have a variable calorie_offset set to 0
  * Map lists 1 and 3 to add calorie_offset.
  * Map lists to form another set of lists made up of difference between values and daily_optimal.
  * Find a value from these whose absolute value is closest to zero, and update calorie_offset to this value. Also pick up the corresponding dish and delete the dish from the list.
  * Repeat last 3 steps over and over until we have 7 dishes selected.

# Challenge 2 (App Store Rankings)

Assumption:
* To be done for apple app store.
* Since I could not find rankings of any app mentioned upon either Play Store or Apple App Store web pages, I am assuming for now that app ratings were the requirement of the challenge and challenge is designed to test knowledge about scrapping. Will really like to have a clarification for this one.
* Therefore a simple scrapper for Apple App Store has been built. I can do the same for Play Store as well if this was the actual requirement of Challenge.

Approach:
* Apple:
  * Use apple search api to get app page url.
  * Scrape app page url for ratings.

# Challenge #3 (Wall of Application Icons)

Approach:
* For Every number select a random number from list ahead to take its position.

# Challenge 4 (Retina Display)

Approach (Discussion Only):

We will use interpolation to do this conversion with interpolation being done in following manner.
* We want to convert a 32 X 32 image into a 64 X 64 image. To do this we imagine a grid overlay over the image in the following manner.
<br/><p align="center">
  <img align="center" src ="https://s18.postimg.org/b8dekkhuh/grid-2.png" /></p><br/>
* We will perform this technique 4 times for each of the layers separately. This layers will be Red, Green, Blue and Alpha. 
* Now we are going to determine the pixels which are marked with ? using interpolation technique.
* We will do this in two phases, first phase consists of only one iteration whereas second phase will be a responsible for finding out all the other pixels by iterating over and over.
* Overall we are going to follow the principle that we should incorporate all known pixels in determination of another pixel which surround it.
* Phase 1:
  * Consider Row 1 and Column 1.
  * We find the value of all pixels marked ? by taking average of the two values at the surrounding pixels whose value is known. This carried out in Row 1.
  * We do the same for Column 1. Average the value at the two surrounding pixels.
  * After this we would have filled in values for all pixels in Row 1 and Column 1.
* Phase 2:
<br/><p align="center">
  <img align="center" src ="https://s10.postimg.org/pirgsfent/grid.png" /></p><br/>
  * In Phase 2 we consider the above given figure to fill in the pixels.
  * Pixels with ?’s are unknowns and marked with only numbers are those whose value is known.
  * Also pixels with ?’s have numbering to differentiate them.
  * In this phase we already have filled in value of ?1, ?4, ?2, ?8.
  * So now we want to determine all other values which could be achieved by interpolating in the following manner.
  * Calculate value of ?3 by averaging all surrounding known pixels. This would be averaging pixels 1, ?1, 2, ?2, 3, 4. A total of six pixels. Similar pattern of pixels will be available for all the pixels resembling ?3 position.
  * Next we calculate value of ?5, ?7. This would now be able to use value from previous calculation of ?3.
  * To calculate ?5, we use all its surrounding known pixels namely ?1, 2, ?4, ?3, 4
  * Similarly for ?7, we would average ?2, ?3, 3, 4, ?8.
  * Now the above steps are repeated to find out all pixels in Row 2, Column 2 sequentially in the same manner.
  * All other rows and columns could be resolved out using the same approach.

