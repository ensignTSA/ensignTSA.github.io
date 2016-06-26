$(document).ready(function(){ // on page load

  $('.slider').slider({full_width: true}); // make slider on 'Home' page take up the entire width of the page

  var image = document.getElementById('image'); // image displayed on 'Learn' page
  var translatebox = document.getElementById('translatebox'); // input box on 'Translate' page
  var translateimg = document.getElementById('translateimg'); // image(s) displayed on 'Translate' page
  var timer1; // initializing global variable for timer for chip 1
  var timer2; // initializing global variable for timer for chip 2
  var timer3; // initializing global variable for timer for chip 3
  var timer4; // initializing global variable for timer for chip 4
  var timer5; // initializing global variable for timer for chip 5

  $('a').click(function(event){ // if a button defined with <a></a> tags is clicked

    if ($(event.target).attr('class') === "waves-effect waves-light btn pink accent-3" || $(event.target).attr('class') === "waves-effect waves-light btn indigo") { // if button is on 'Learn' page
      clearTimeout(timer1); // clear timer1
clearTimeout(timer2); // clear timer2
clearTimeout(timer3); // clear timer3
clearTimeout(timer4); // clear timer4
clearTimeout(timer5); // clear timer5
$('#chip1').removeClass('indigo white-text'); // reset appearance of chip 1
$('#chip2').removeClass('indigo white-text'); // reset appearance of chip 2
$('#chip3').removeClass('indigo white-text'); // reset appearance of chip 3
$('#chip4').removeClass('indigo white-text'); // reset appearance of chip 4
$('#chip5').removeClass('indigo white-text'); // reset appearance of chip 5
	  image.innerHTML = "<img src='pngs edited/" + event.target.id + ".PNG' width='450px' height='450px'>"; // change displayed image based on button clicked
	  timer1 = setTimeout(function () { // after 1 second change appearance of chip 1
        $('#chip1').addClass('indigo white-text');
      }, 1000);
timer2 = setTimeout(function () { // after 2 seconds change appearance of chip 2
        $('#chip2').addClass('indigo white-text');
      }, 2000);
timer3 = setTimeout(function () { // after 3 seconds change appearance of chip 3
        $('#chip3').addClass('indigo white-text');
      }, 3000);
timer4 = setTimeout(function () { // after 4 seconds change appearance of chip 4
        $('#chip4').addClass('indigo white-text');
      }, 4000);
timer5 = setTimeout(function () { // after 5 seconds change appearance of chip 5
        $('#chip5').addClass('indigo white-text');
      }, 5000);
    } else if ($(event.target).attr('class') === "waves-effect waves-indigo btn-flat") { // if button is 'Clear Message' on 'Translate' page
      $(translatebox).val(''); // clear input box
      translateimg.innerHTML = ""; // clear displayed images
      Materialize.toast('Message cleared.', 2000); // toast alert lasting for 2 seconds
    }

  });

  $('button').click(function(event){ // if a button defined with <button></button> tags is clicked

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
