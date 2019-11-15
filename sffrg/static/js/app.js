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

    // Stores user input in the form so they don't have to retype all of it if an error occurs
    if ($('#RegistrationSteps').length > 0) {
        $('[name=first_name]').val(localStorage.getItem("first_name"));
        $('[name=middle_name]').val(localStorage.getItem("middle_name"));
        $('[name=last_name]').val(localStorage.getItem("last_name"));
        $('[name=email]').val(localStorage.getItem("email"));
        $('[name=username]').val(localStorage.getItem("username"));

        // $("#InputCitizenF").prop("checked", localStorage.getItem('citizenf'));
        // $("#InputCitizenT").prop("checked", localStorage.getItem('citizent'));
        // $("#InputDisqualifiedF").prop("checked", localStorage.getItem('disqualifiedf'));
        // $("#InputDisqualifiedT").prop("checked", localStorage.getItem('disqualifiedt'));
        // $("#active_milF").prop("checked", localStorage.getItem('active_milf'));
        // $("#active_milT").prop("checked", localStorage.getItem('active_milt'));

        $('[name=gender]').val(localStorage.getItem("gender"));
        $('[name=street]').val(localStorage.getItem("street"));
        $('[name=city]').val(localStorage.getItem("city"));
        $('[name=zip_code]').val(localStorage.getItem("zip_code"));

        $('#firstReg').submit(function(){
            // var fname = $('#InputNamesf').val();
            // localStorage.setItem("fname", fname);
            localStorage.setItem("first_name", $('[name=first_name]').val());
            localStorage.setItem("middle_name", $('[name=middle_name]').val());
            localStorage.setItem("last_name", $('[name=last_name]').val());
            localStorage.setItem("email", $('[name=email]').val());
            localStorage.setItem("username", $('[name=username]').val());

            // localStorage.setItem('citizenf', $("#InputCitizenF").prop("checked"));
            // localStorage.setItem('citizent', $("#InputCitizenT").prop("checked"));
            // localStorage.setItem('disqualifiedf', $("#InputDisqualifiedF").prop("checked"));
            // localStorage.setItem('disqualifiedt', $("#InputDisqualifiedT").prop("checked"));
            // localStorage.setItem('active_milf', $("#active_milF").prop("checked"));
            // localStorage.setItem('active_milt', $("#active_milT").prop("checked"));

            localStorage.setItem("citizen", $('[name=citizen]').val());
            localStorage.setItem("gender", $('[name=gender]').val());
            localStorage.setItem("street", $('[name=street]').val());
            localStorage.setItem("city", $('[name=city]').val());
            localStorage.setItem("zip_code", $('[name=zip_code]').val());
        });
    }

    else
    {
        window.onunload = function() {
            alert("Leaving!");
            localStorage.clear();
            localStorage.removeItem('citizenf');
            localStorage.removeItem('citizent');
            localStorage.removeItem('disqualifiedf');
            localStorage.removeItem('disqualifiedt');
            localStorage.removeItem('active_milf');
            localStorage.removeItem('active_milt');
        }
    }


    $('#descriptionModal').on('shown.bs.modal', function() {
        $('#learnMore').trigger('focus')
    })

});
