/**
 * Created by Administrator on 2016/12/1.
 */

// post方式不同于get方式可以被django直接得到，因为django为post加入了csrf保护，
// 详细的文档地址https://docs.djangoproject.com/en/dev/ref/csrf/
//
// 注释:在最新版本中，在setting.py里'django.middleware.csrf.CsrfViewMiddleware',
// 默认是使用中的，如果没有请自行添加,并且确保此引用在其他所有viewware前面
// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie != '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
//
// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }


var tableLine = function () {
    $('.line').mouseover(function () {
        if (!$(this).hasClass('selectline')) {
            $(this).css('cursor', 'pointer').css('background', '#F5F5F5')
        }
    }).mouseout(function () {
        if (!$(this).hasClass('selectline')) {
            $(this).css('cursor', 'default').css('background', '')
        }
    }).click(function () {
        if ($(this).hasClass('selectline')) {
            $(this).removeClass('selectline').css('background', '')
        } else {
            $(this).addClass('selectline').css('background', 'red')
        }
    })
}


$(function () {
    // tableLine()
})
