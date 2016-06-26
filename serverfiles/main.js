$(document).ready(function() { // on page load

    $('.slider').slider({
        full_width: true
    }); // make slider on 'Home' page take up the entire width of the page

    var image = document.getElementById('image'); // image displayed on 'Learn' page
    var translatebox = document.getElementById('translatebox'); // input box on 'Translate' page
    var translateimg = document.getElementById('translateimg'); // image(s) displayed on 'Translate' page


    $('a').click(function(event) { // if a button defined with <a></a> tags is clicked

        if ($(event.target).attr('class') === "waves-effect waves-light btn pink accent-3" || $(event.target).attr('class') === "waves-effect waves-light btn indigo") { // if button is on 'Learn' page

            image.innerHTML = "<img src='pngs edited/" + event.target.id + ".PNG' width='450px' height='450px'>"; // change displayed image based on button clicked

        } else if ($(event.target).attr('class') === "waves-effect waves-indigo btn-flat") { // if button is 'Clear Message' on 'Translate' page
            $(translatebox).val(''); // clear input box
            translateimg.innerHTML = ""; // clear displayed images
            Materialize.toast('Message cleared.', 2000); // toast alert lasting for 2 seconds
        }

    });

    $('button').click(function(event) { // if a button defined with <button></button> tags is clicked

        if ($(event.target).attr('id') === "translate") { // double checking that it is the 'Translate' button on the 'Translate' page
            translateimg.innerHTML = ""; // clear displayed images first
            var chars = translatebox.value.toUpperCase().replace(/\s+/g, ''); // take input from input box, convert all letters to uppercase, remove all whitespace
            if (chars.match(/^[a-zA-Z0-9]+$/i)) { // if input string consists only of alphanumeric characters
                for (var i = 0, len = chars.length; i < len; i++) { // loop through each character in the string
                    translateimg.innerHTML += "<img src='pngs edited/" + chars.charAt(i) + ".PNG' width='300px' height='300px'>"; // display corresponding picture file
                }
                $(translatebox).val(''); // clear input box
            } else if (chars === "") { // if nothing was inputted, but 'Translate' button was still clicked
                Materialize.toast('Please enter a message.', 2000); // toast alert lasting for 2 seconds
            } else { // if non-alphanumeric characters (e.g., punctuation) were inputted
                Materialize.toast('Please enter only alphanumeric characters.', 3000); // toat alert lasting 3 seconds
            }
        }

    });

});

responseDiv3 = document.getElementById("response2"); //used to easily reference the div that contains the response to the practice option
var alphaNumericArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C', 'D', 'E', 'F', 'G', "H", 'I', "J", 'K', "L", "M", "N", "O", 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', "X", 'Y', 'Z']; //used for randomly generating characters
var IntervalID; //used for ending certain loops
var rand; //a random character, used for the practice page
var disabled = false; //boolean used to prevent the user from accessing multiple learn characters simultaneously

function disableAll() // disables all the buttons to prevent the user from clicking too many in quick succession
{
    if (disabled == false) {
        disabled = true;
        setTimeout(function() {
            disabled = false
        }, 6000);
    }
}

function enablePractice() //reenables the practice button
{
    document.getElementById('practicebtn').disabled = false;
}

function startCount() { //starts the practice mode

    alphaNumericArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C', 'D', 'E', 'F', 'G', "H", 'I', "J", 'K', "L", "M", "N", "O", 'P', "Q", 'R', 'S', 'T', 'U', 'V', 'W', "X", 'Y', 'Z'];
	
    rand = alphaNumericArray[Math.floor(Math.random() * alphaNumericArray.length)]; //generates random value
	
    if (submitImage('Practice')) //runs submit image and checks for return value
    {
        console.log('hi')
        alphaNumericArray.splice(alphaNumericArray.indexOf(rand), 1); //if user made correct sign, remove rand from array
        rand = alphaNumericArray[Math.floor(Math.random() * alphaNumericArray.length)]; //generate new rand
    }
	
    IntervalID = setInterval(function() { //every 8 seconds, repeat the script
        if ((responseDiv3.innerHTML) == "Correct.") //almost the same script as above
        {
            alphaNumericArray.splice(alphaNumericArray.indexOf(rand), 1);
            console.log('choosing new rand');
            rand = alphaNumericArray[Math.floor(Math.random() * alphaNumericArray.length)];
        }
		
        if (alphaNumericArray != null && alphaNumericArray.length >= 1) {
            console.log(alphaNumericArray)
            submitImage('Practice');
        } else {
            stopCount();
        }
    }, 8000);
}

function stopCount() { //stops practice
    clearInterval(IntervalID);
    //letterdiv = document.getElementById('letterdiv');
    //letterdiv.innerHTML = '';
    //response2 = document.getElementById('response2');
    //response2.innerHTML = '';
}

var timer1; // initializing global variable for timer for chip 1
var timer2; // initializing global variable for timer for chip 2
var timer3; // initializing global variable for timer for chip 3
var timer4; // initializing global variable for timer for chip 4
var timer5; // initializing global variable for timer for chip 5
function loading(querySelector) //loads the webcam capture
{
    var video = document.querySelector(querySelector); //gets video element, saves as variable
    navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia; //sets up getUserMedia
    navigator.getUserMedia({
        video: true
    }, function() { //asks for permission
        //webcam available 
    }, function() { //if permission not given
        chips = document.getElementsByClassName('chip') //make chips disappear
        for (var i = 0, il = chips.length; i < il; i++) {
            chips[i].style.visibility = 'hidden';
            disabled = true;
        }
        boxes = document.getElementsByClassName('mybox') //make boxes disappear
        for (var i = 0, il = boxes.length; i < il; i++) {
            boxes[i].style.visibility = 'hidden';
        }
        responseDiv1 = document.getElementById('response'); //change responses to show informative messages
        responseDiv2 = document.getElementById('response2');
        responseDiv1.innerHTML = 'You need a webcam to use this feature. Please plug a webcam into your computer and refresh the page.';
        responseDiv1.style.color = 'black';
        responseDiv2.innerHTML = 'You need a webcam to use this feature. Please plug a webcam into your computer and refresh the page.';
        responseDiv2.style.color = "black";

        //webcam not available
    });
    if (navigator.getUserMedia) //gets media from user
    {
        var thevid = {
            video: true,
            audio: false
        };
        navigator.getUserMedia(thevid, handleVideo, forError) //sets up video input
    }



    function handleVideo(localmediastream) {
        video.src = window.URL.createObjectURL(localmediastream); //gets video from webcam
    }

    function forError(e) {
        // mandatory error handler
    }

}

function submitImage(letter) //submits sign to server for checking
{
    if (disabled == false) //if disabled is true, the function does nothing
    {
        responseDiv3 = document.getElementById("response2"); //unnecessary line, can delete later
        clearTimeout(timer1); // clear timer1
        clearTimeout(timer2); // clear timer2
        clearTimeout(timer3); // clear timer3
        clearTimeout(timer4); // clear timer4
        clearTimeout(timer5); // clear timer5
        $('.chip1').removeClass('indigo white-text'); // reset appearance of chip 1
        $('.chip2').removeClass('indigo white-text'); // reset appearance of chip 2
        $('.chip3').removeClass('indigo white-text'); // reset appearance of chip 3
        $('.chip4').removeClass('indigo white-text'); // reset appearance of chip 4
        $('.chip5').removeClass('indigo white-text'); // reset appearance of chip 5

        function readBody(xhr) { //function to read body of POST request
            var data;
            if (!xhr.responseType || xhr.responseType === "text") {
                data = xhr.responseText;
            } else if (xhr.responseType === "document") {
                data = xhr.responseXML;
            } else {
                data = xhr.response;
            }
            return data;
        }
        if (letter == "Practice") //if the practice parameter is passed, replace it with a random latter and use practice page instead of learn page
        {
            responseDiv = document.getElementById('response2');
            letterdiv = document.getElementById('letterdiv');
        } else {
            responseDiv = document.getElementById('response'); //otherwise, proceed normally and use learn page
        }
        canvas = document.getElementById('canvas'); //gets canvas
        video = document.getElementById('forVid'); //gets video
        console.log(video.width);
        console.log(video.height);
        canvas.style.display = "none";
        canvas.width = 600; //determines canvas width
        canvas.height = 400; //determines canvas height

        if (letter == "Practice") {
            letterdiv.innerHTML = ('Please make the character ' + rand);
            timer1 = setTimeout(function() { // after 1 second change appearance of chip 1
                $('#chip6').addClass('indigo white-text');
            }, 1000);
            timer2 = setTimeout(function() { // after 2 seconds change appearance of chip 2
                $('#chip7').addClass('indigo white-text');
            }, 2000);
            timer3 = setTimeout(function() { // after 3 seconds change appearance of chip 3
                $('#chip8').addClass('indigo white-text');
            }, 3000);
            timer4 = setTimeout(function() { // after 4 seconds change appearance of chip 4
                $('#chip9').addClass('indigo white-text');
            }, 4000);
            timer5 = setTimeout(function() { // after 5 seconds change appearance of chip 5
                $('#chip10').addClass('indigo white-text');
            }, 5000);
        } else {
            responseDiv.innerHTML = ('Please make the character ' + letter);
            timer1 = setTimeout(function() { // after 1 second change appearance of chip 1
                $('#chip1').addClass('indigo white-text');
            }, 1000);
            timer2 = setTimeout(function() { // after 2 seconds change appearance of chip 2
                $('#chip2').addClass('indigo white-text');
            }, 2000);
            timer3 = setTimeout(function() { // after 3 seconds change appearance of chip 3
                $('#chip3').addClass('indigo white-text');
            }, 3000);
            timer4 = setTimeout(function() { // after 4 seconds change appearance of chip 4
                $('#chip4').addClass('indigo white-text');
            }, 4000);
            timer5 = setTimeout(function() { // after 5 seconds change appearance of chip 5
                $('#chip5').addClass('indigo white-text');
            }, 5000);
        }

        setTimeout(function() {
            var context = canvas.getContext('2d'); //gets context from canvas
            context.clearRect(0, 0, canvas.width, canvas.height); //handles dimensions

            context.fillStyle = "#FFFFFF"; //default image is white square
            context.fillRect(0, 0, canvas.width, canvas.height); //handles canvas dimensions

            context.drawImage(video, 0, 0, canvas.width, canvas.height); //gets picture from canvas

            var data = canvas.toDataURL('image/jpeg', 1); //converts image to URL data
            var ajax = new XMLHttpRequest();
            ajax.open("POST", 'https://ensign.hthswd.org:8085/process_file', false); //opens POST request with server; false means it is SYNCHRONOUS!!!!!!!!
            ajax.onreadystatechange = function() {
                console.log(ajax.responseText);
            }
            ajax.setRequestHeader('Content-Type', 'application/upload'); //sets up POST request
            if (letter == "Practice") {
                ajax.send(rand + "imgData=" + data);
            } else {
                ajax.send(letter + "imgData=" + data); //sends data to server
            }
            console.log(data.length); //logs length of data to console, used for debugging
            responseDiv.innerHTML = readBody(ajax);
            if ((responseDiv3.innerHTML) == "Correct.") {
                console.log("great"); //logs success
                return true;
            } else {
                return false;
            }
        }, 6000); //6 second delay to give user time to position hand

    }
}