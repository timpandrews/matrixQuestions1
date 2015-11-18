function init() {

    //alert("hello")
    var i = 1;
    var maxIterations = 22; //******** Set to 100 when done ********

    var randomNumberArray = []
    var EMAArray = []

    var repeater = setInterval(function () {
        if (i <= maxIterations) {
            //alert(i)

            var randomNumber = getRandomNumber()
            randomNumberArray.push(randomNumber)

            var EMA = getEMA(randomNumberArray, EMAArray)
            EMAArray.push(EMA)

            buildTable(randomNumberArray, EMAArray)

            i++;
        } else {
            //alert("done")
            clearInterval(repeater);
        }
    }, 500);

}

function getEMA(randomNumberArray, EMAArray) {

    /* Exponential Move Average (EMA)
        Current EMA= ((Price(current) - previous EMA)) X multiplier) + previous EMA.
        Source: http://www.investopedia.com/articles/trading/10/simple-exponential-moving-averages-compare. asp
    */

    var EMA
    var previousEMA
    var sampleSize = 20
    var smoothingFactor = 2 / (1 + sampleSize)
    var currentValue = randomNumberArray[randomNumberArray.length - 1]

    //alert(randomNumberArray)
    //Get 1st EMA with 1st record
    if (randomNumberArray.length <= 1) {
        EMA = randomNumberArray[0]
    } else {
        previousEMA = EMAArray[randomNumberArray.length-2]
        EMA = (((currentValue - previousEMA) * smoothingFactor) + previousEMA)
    }

    return EMA

}

function getRandomNumber() {

    var randomNumber = Math.floor(Math.random() * 10) + 1

    //alert(randomNumber)

    return randomNumber;

}

function buildTable(randomNumberArray, EMAArray) {

    //alert(randomNumberArray)
    var arrayLength = randomNumberArray.length
    var relativeToEMA
    //alert(arrayLength)


    var html = "<table id='resultsTable'>"
    html+=          "<thead>"
    html+=              "<tr>"
    html+=                  "<th>Random Number</th>"
    html+=                  "<th>EMA</th>"
    html+=              "</tr>"
    html+=          "</thead>"
    html +=     "<tbody>"

    /* Start Loop 10 records from the end (showing last 10 records), unless there
       are less then 10 records then start at the 1st record and show all records */
    var startLoop = arrayLength - 10
    if (startLoop < 0) {
        startLoop = 0
    }

    for (x = startLoop ; x < arrayLength; x++) {

        if (randomNumberArray[x] > EMAArray[x]) {
            relativeToEMA = "aboveEMA"
        } else if (randomNumberArray[x] < EMAArray[x]) {
            relativeToEMA = "belowEMA"
        } else if (randomNumberArray[x] = EMAArray[x]) {
            relativeToEMA = "equalToEMA"
        }

        html +=     "<tr class='" + relativeToEMA + "'>"
        html+=          "<td>" + randomNumberArray[x] +"</td>"
        html +=         "<td>" + Math.round(EMAArray[x] * 100) / 100 + "</td>"
        html+=      "</tr>"

    }

    html+=          "</tbody>"
    html+=      "</table>"

    var body = document.getElementsByTagName("body")[0];

    //alert(html)
    body.innerHTML = html

}
