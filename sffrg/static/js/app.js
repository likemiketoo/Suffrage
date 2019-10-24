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
