$(document).ready(function() {
    $("#searchInput").focus();

    const SEARCH_INPUT_ID = "#searchInput";

    var pages = ["home", "projects", "resume", "randwords", "uttt", "game"];

    console.log(pages);

    if (window.location.hash) {
        console.log(window.location.hash);
        if (pages.indexOf(window.location.hash.substring(1)) > -1) {
            console.log(1);
            $("#content").load("/", {
                hashID: window.location.hash.substring(1)
            });
        } else {
            console.log(2);
            $("#content").load("/default");
            location.hash = "home";
        }
    } else {
        $("#content").load("/default");
    }

    $("#searchButton").click(function() {
        var searchInputText = $(SEARCH_INPUT_ID).val().toLowerCase();
        if (pages.indexOf(searchInputText) > -1) {
            location.hash = searchInputText;
        }
        $(SEARCH_INPUT_ID).val("");
    });
    $(SEARCH_INPUT_ID).on('keyup', function(e) {
        var searchInputText = $(SEARCH_INPUT_ID).val().toLowerCase();
        if (e.keyCode == 13) {
            if (pages.indexOf(searchInputText) > -1) {
                location.hash = searchInputText;
            }
            $(SEARCH_INPUT_ID).val("");
        }
    });

    $(window).on('hashchange', function() {
        $("#content").load("/", {
            hashID: window.location.hash.substring(1)
        });
    });

});
