// Adding required libraries

const yargs = require('yargs');
const axios = require('axios');

//Settings for input parameters

const argv = yargs
    .options({
        a: {
            demand: true,
            alias: 'address',
            describe: 'Address to fetch weather for',
            string: true
        }
    })
    .help()
    .alias('help', 'h')
    .argv;

//Getting the address from url and encoding it

var encAddress = encodeURIComponent(argv.address);
var geoCodeurl = `https://maps.googleapis.com/maps/api/geocode/json?address=${encAddress}`;

//Using axios to hit the api and get the weather info

axios.get(geoCodeurl).then((response) => {
    if (response.data.status === 'ZERO_RESULTS') {
        throw new Error('Unable to fetch the weather for given address')
    }
    var lat = response.data.results[0].geometry.location.lat;
    var lng = response.data.results[0].geometry.location.lng;
    console.log(response.data.results[0].formatted_address);
    var waetherUrl = `https://api.darksky.net/forecast/9a408dc945b3a1cff7ffc66679ae0a0a/${lat},${lng}`;
    return axios.get(waetherUrl);
}).then((response) => {
    var temperature = response.data.currently.temperature;
    var apparentTemperature = response.data.currently.apparentTemperature;
    console.log(`Current temperature : ${temperature}, Feels Like: ${apparentTemperature}`);
}).catch((e) => {
    if (e.code === 'ENOTFOUND') {
        console.log("Unable to Connect to API");
    } else {
        console.log(e);
    }
});
