# LoLde by Information Theory

## Obtaining the the champion files
Go to www.loldle.net and view the page source. The minified bundle is named differently each time, but can be found included in the end script as `app.xxx.js`. Save this file and look for the variable containing the champion information. It is also minified to a new variable upon each update, but an easy way to find it is to search for the `championId` property which is only found and used in this variable. Remark that newer champions added do not have this property as it is unused in the code, and it may be removed later.
For now, the following regex should do the trick
```regex
=(\[\{_id:"[^{}]+championId:".+?\}\])=(\[\{.+championId:".+\}\])
```
*Remember that the javascript is UTF-8 encoded due to the different languages contained within.*

Once this is done, you can put the javascript object through [Javascript Object to JSON Converter](https://www.convertsimple.com/convert-javascript-to-json/) and save it. Not the cleanest solution.