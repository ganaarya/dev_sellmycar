var getDynamicWidth = $('.my-jumbotron-color').innerWidth();
var getScreenWidth = 0;
// $('.jumbotron').css('padding-top','5px')

window.onload = function() {
  getScreenWidth = screen.width;
};

function initialLoad() {
  $('.my-navbar-style').width(getScreenWidth - (getScreenWidth*0.2));
  if ($(window).width() < getScreenWidth) {
    $('.my-container').width(getScreenWidth)
  }
  $('.my-navbar-style').css('margin','0 auto')
  $('.my-img').css('padding-left',$('.my-navbar-style').css('margin-left'))
}

function setToCenter() {
  if ($(window).width() > getScreenWidth) {
    $('.my-container').width($(window).width())
  }else if ($(window).width() <= getScreenWidth) {
    $('.my-container').width(getScreenWidth)
  }
  $('.my-navbar-style').css('margin','0 auto')
  $('.my-img').css('padding-left',$('.my-navbar-style').css('margin-left'))

}

$(window).on("load",initialLoad);
$(window).on("load",setToCenter);

window.onresize = setToCenter;
