$(document).ready(function() {
  var canSync = true;

  $("#sync-pub-btn").click(function(){
    if (canSync) {
      canSync = false;
      var sendData = {
        username: $('#sync-username').val(),
        password: $('#sync-password').val()
      }
      
      $.post("/sync-pubs",
        sendData)
        .done(function(msg){ 
          alert('successfully added pub keys');
          canSync = true;
         })
        .fail(function(xhr, status, error) {
          canSync = true;
        });
    } else {
      alert("Please wait to sync");
    }
  }); 


});
