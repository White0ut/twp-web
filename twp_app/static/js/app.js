$.getScript('static/js/includes.js');

$(document).ready(function () {
  var canSync = true;

  /**
   * This button will sync the pub keys by calling a backend API with the username and password
   * of that email in the body of the POST request.
   */
  $("#sync-pub-btn").click(function () {
    if (canSync) {
      canSync = false;
      var sendData = {
        username: $('#sync-username').val(),
        password: $('#sync-password').val()
      }

      $.post("/sync-pubs",
        sendData)
        .done(function (msg) {
          flash('Successfully synced users');
        })
        .fail(function (xhr, status, error) {
          flash('Failed to sync users ' + error);
        }).always(function () {
          canSync = true;
        });

    } else {
      alert("Please wait to sync");
    }
  });

  /**
   * Adds an assignment to the config. This will create repos for the user.
   */
  $('#add-assignment-btn').click(function () {
    var course = $('#add-course').val();
    var assignment = $('#add-assignment').val();

    $.post('/api/conf/assignment',
      {
        "course": course,
        "assignment": assignment
      })
      .done(function (msg) {
        $('#assignment-table tbody').append(
          String.format('<tr>\
            <td>{0}</td>\
            <td>{1}</td>\
            <td><a id="{0}-{1}-status" onClick="updateStatus(\'{0}\', \'{0}\')">open</a></td>\
          </tr>', course, assignment)
        );
      })
      .fail(function (xhr, status, error) {
        flash('Failed to add assignment.');
      });

    $('#add-course').val('');
    $('#add-assignment').val('');
  });

  /**
   * Adds a TA entry, please ensure there is a .pub key already associated with the TA in question
   */
  $('#add-ta-btn').click(function () {
    var ta = $('#add-ta').val();

    $.post('/api/conf/ta',
      {
        "ta": ta
      })
      .done(function (msg) {
        $('#collapse-tas ul').append('<li class="list-group-item">' + ta + '</li>');
      })
      .fail(function (xhr, status, error) {
        flash('Failed to add TA.');
      });

    console.log('ta: ' + ta);
    $('#add-ta').val('');
  });

  /**
   * Adds a professor entry, please ensure there is a .pub key already associated with the Prof in question
   */
  $('#add-prof-btn').click(function () {
    var prof = $('#add-prof').val();

    $.post('/api/conf/prof',
      {
        "prof": prof
      })
      .done(function (msg) {
        $('#collapse-profs ul').append('<li class="list-group-item">' + prof + '</li>');
      })
      .fail(function (xhr, status, error) {
        flash('Failed to add Professor.');
      });

    console.log('prof: ' + prof);
    $('#add-prof').val('');
  });

});
// End document.ready

function updateStatus(course, assn, stat) {
  var id = '#' + course + '-' + assn + '-status';
  var newStat = $(id).html() === 'open' ? 'close' : 'open';
  console.log('setting to: ' + newStat);

  $.post("/api/conf/update_status",
    {
      "course": course,
      "assignment": assn,
      "status": newStat
    })
    .done(function (msg) {
      $(id).html(newStat);
    })
    .fail(function (xhr, status, error) {
      flash('Failed to update assignment.');
    });
}

var flash = function (msg) {
  $("#page-container").prepend('<div class="well well-sm">' + msg + '</div>').fadeIn('slow');
}
