document.getElementById("ar-link").addEventListener("message", function (event) {   
    if (event.data == "_apple_ar_quicklook_button_tapped") {
        window.location.assign("https://developer.apple.com/documentation/arkit/previewing_a_model_with_ar_quick_look");
    }
}, false);


document.getElementById("ar-link-3").addEventListener("message", function (event) {   
    if (event.data == "_apple_ar_quicklook_button_tapped") {
        window.location.assign("https://developer.apple.com/documentation/arkit/previewing_a_model_with_ar_quick_look");
    }
}, false);