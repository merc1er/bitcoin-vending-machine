$(document).ready(function () {
    console.log("ready");
    verify_payment();
    setInterval(verify_payment, 1000); // verifies every second

    function verify_payment(){
        $.getJSON("https://rest.bitbox.earth/v1/address/details/bitcoincash%3Aqz8zcxumuzd8fx4cxc73qlhs8kta4jv6wu9knfn567", function (data) {
            var balance = data.unconfirmedBalance;
            console.log(balance);
            // document.getElementById('price-ticker-bch').innerHTML = "$" + price;
        })
    };

});