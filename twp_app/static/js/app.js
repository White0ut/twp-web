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
          flash('Successfully synced users');
         })
        .fail(function(xhr, status, error) {
          flash('Failed to sync users ' + error);
        }).always(function() {
          canSync = true;
        });

    } else {
      alert("Please wait to sync");
    }
  }); 

});

function updateStatus(course, assn, stat) {
  var newStat = stat === 'open' ? 'close' : 'open';
  $.post("/api/conf/update_status",
    {
      "course" : course,
      "assignment" : assn,
      "status" : newStat
    })
    .done(function(msg) {
      $('#'+course+'-'+assn+'-status').html(newStat);
    })
    .fail(function(xhr, status, error) {
      flash('Failed to update assignment');
    });
}

var flash = function(msg) {
  $("#page-container").prepend('<div class="well well-sm">'+msg+'</div>').fadeIn('slow');
}
