# LoLde by Information Theory
Finding the best answers for the Wordle-clone [LoLdle](www.loldle.net) by use of information theory.
Contains an algorithm which guesses the champion with the most amount of information in Shannon bits every turn. It gueses almost every champion in less than 3 tries. This repository contains the following main files:
* `loldle.py`: A library containing functions for limiting the champion pool to available champions and calculating the best guesses from that pool.
* `simulate.py`: A simulation of every game of LoLdle using the algorithm. Produces the guess order seen in `/results/guess-order.csv`
* `graph.py`: Produces the graphs found in `/results/guess-order.csv` for use in the my [article about the concept.](https://itmunk.netlify.app/posts/loldle-information-theory/)

`graph.py` requires [matplotlib](https://matplotlib.org/) and `simulate.py` requires [tqdm](https://github.com/tqdm/tqdm) for the progress bar, since it can take some time (32 s on my computer).

## Obtaining the the champion files
A champion data file is included in the repository in `resources/loldle-champ-data.json` which is obtained from the LoLdle website javascript. If you wish to update the champion list, follow these steps:


Go to www.loldle.net and view the page source. The minified bundle is named differently each time, but can be found included in the end script as `app.xxx.js`. Save this file and look for the variable containing the champion information. It is also minified to a new variable upon each update, but an easy way to find it is to search for the `championId` property which is only found and used in this variable. Remark that newer champions added do not have this property as it is unused in the code, and it may be removed later.
For now, the following regex should do the trick
```regex
=(\[\{_id:"[^{}]+championId:".+?\}\])
```
*Remember that the javascript is UTF-8 encoded due to the different languages contained within.*
This regex is implemented in `resources/extract-champlist.py` which can be used to extract the javascript object. Once this is done, you can put the javascript object through [Javascript Object to JSON Converter](https://www.convertsimple.com/convert-javascript-to-json/) and save it. Not the cleanest solution.