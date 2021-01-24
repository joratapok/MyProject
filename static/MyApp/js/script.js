$(document).ready(function() {
	$('.header__burger').click(function(event) {
		$('.header__burger, .header__menu').toggleClass('active');
		$('body').toggleClass('lock');
	});
});


var mybutton = $("#myBtn");

$(window).scroll(function() {
  if ($(window).scrollTop() > 150) {
    mybutton.addClass('show-topbtn');
  } else {
    mybutton.removeClass('show-topbtn');
  }
});

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

