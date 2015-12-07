var app = {
  invert : function(){
    var str = $('#str_invert_input');
    var inputVal = str.val();
    var encoded = encodeURI(inputVal);

    var result = $('#result');

    // Add the web service URL
    $.get( "http://127.0.0.1:8081/"+encoded, function( data ) {

    result.html(data);

    });
  }

}
