//Animates slide ou menu
$("#menu-toggle").click(function(e)
{
	e.preventDefault();
	$(".mainContentWrapper").toggleClass("toggled");
 });

var prevScrollpos = 1;

$(window).scroll(function()
{
	var currentScrollPos = window.pageYOffset;
	if (prevScrollpos > currentScrollPos)
	{
		document.getElementById('titleBar').style.top = "0";
	}

	else
	{
		document.getElementById('titleBar').style.top = "-50px";
	}
	prevScrollpos = currentScrollPos;
});


$( document ).ready(function() {
    $("#page2Buttons").hide();
    // $("#prevButton").hide();
    // $("#nextButton2").hide();
    $("#prevButton2").hide();
    $("#submitButton").hide();
    $("#form2").hide();
    $("#form3").hide();
    $("#restoredQuestion").hide();

    // If voter isn't a citizen hide and alert
     $('#InputCitizenT').click(function(){
        // $("#namesRow").toggle();
       $("#voteCitizen").show();
        $("#page2Buttons").show();
    });

    $('#InputCitizenF').click(function(){
        $("#voteCitizen").hide();
        $("page2Buttons").hide();
        alert("You cannot register to vote if you're not a US citizen.");
    });

    // If user is disqualified
    $('#InputDisqualifiedT').click(function(){
        $("#restoredQuestion").show();
    });

    $('#InputDisqualifiedF').click(function(){
        $("#restoredQuestion").hide();
        // $('input[name="restored"]').prop('checked', false);
    });

    // If users rights were restored
    $('#InputRestoredT').click(function(){
        $("#page2Buttons").show();
    });

    $('#InputRestoredF').click(function(){
        $("#page2Buttons").hide();
        alert("You cannot register to vote if your right to vote has not been restored.");
    });



    // Page 1
    $('#nextButton1').click(function(){
        $("#form1").hide();
        $("#nextButton1").hide();

        $("#form2").show();
        $("#page2Buttons").show();
        // $("#prevButton").show();
        // $("#nextButton2").show();
    });

    // Page 2
    $('#prevButton').click(function(){
        $("#form2").hide();
        $("#page2Buttons").hide();
        // $("#prevButton").hide();
        // $("#nextButton2").hide();
        $("#form1").show();
        $("#nextButton1").show();
    });

    $('#nextButton2').click(function(){
        $("#form2").hide();
        $("#nextButton2").hide();
        $("#prevButton").hide();

        $("#form3").show();
        $("#prevButton2").show();
        $("#submitButton").show();
    });

    // Page 3
    $('#prevButton2').click(function(){
        $("#form3").hide();
        $("#submitButton").hide();
        $("#prevButton2").hide();

        // $("#nextButton2").hide();

        $("#form2").show();
        $("#nextButton2").show();
        $("#prevButton").show();
    });

    // $('#InputNamesf').val(localStorage.getItem("fname"));
    // $('#firstReg').submit(function(){
    //    var fname = $('#InputNamesf').val();
    //    alert(fname);
    //    localStorage.setItem("fname", fname);
    // });


});
