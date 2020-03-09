const csvtojson = require("csvtojson")
const jsontocsv = require('jsontocsv')
const fs = require("fs")

csvtojson().fromFile("./zomato.csv").then(zomato => {
    console.log(zomato)
});