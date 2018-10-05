$(document).ready(function() {
    $("#searchInput").focus();

    var pages = ["home", "projects", "resume"];

    console.log(pages);

    if(window.location.hash){
      console.log(window.location.hash);
      if(pages.indexOf(window.location.hash.substring(1)) > -1){
          console.log(1);
          $("#content").load("/", {hashID: window.location.hash.substring(1)});
      } else {
          console.log(2);
          $("#content").load("/default");
          location.hash = "home";
      }
    } else {
      $("#content").load("/default");
    }

    $("#searchButton").click(function() {
      if(pages.indexOf($("#searchInput").val().toLowerCase()) > -1){
        location.hash = $("#searchInput").val().toLowerCase();
      }
      $("#searchInput").val("");
    });
    $("#searchInput").on('keyup', function(e) {
      if (e.keyCode == 13) {
        if(pages.indexOf($("#searchInput").val().toLowerCase()) > -1){
          location.hash = $("#searchInput").val().toLowerCase();
        }
        $("#searchInput").val("");
      }
    });

    $(window).on('hashchange', function(){
      $("#content").load("/", {hashID: window.location.hash.substring(1)});
    });

  });
