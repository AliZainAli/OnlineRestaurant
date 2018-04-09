var sum =0 ;
var total=0 ;
var i = 1 ;

function additem ( name , price ) {
    document.getElementById("selecteditems").innerHTML += "<p id='selected"+i+"'  >"  +  name  ;
    document.getElementById("pr").innerHTML += "<p id='p"+i+"'  >"  +  price  ;
    document.getElementById("removebtn").innerHTML += "<p id='B"+i+"'>" + "<button id='selected"+i+"' class='btn btn-danger' onclick='removeitem("+i+" , "+price+" ) ' style='font-size: 15px; height: 20px; padding: 0px 0px 0px 0px;' >Remove</button> " ;
    i++ ;
    sum += price ;
    document.getElementById("bill").innerHTML = sum;
    }

function removeitem ( i , price ) {

    document.getElementById("selected"+i ).innerHTML="" ;
    document.getElementById("p"+i ).innerHTML="" ;
    document.getElementById("B"+i ).innerHTML="" ;
    i-- ;
    sum -= price ;
    document.getElementById("bill").innerHTML = sum;
    }

function finish() {

    location.href = "Login.html";
}

function addclass ( elem ) {
    // get all 'a' elements
    var a = document.getElementsByTagName('a');
    // loop through all 'a' elements
    for (i = 0; i < a.length; i++) {
        // Remove the class 'active' if it exists
        a[i].classList.remove('current')  ;
    }
    // add 'active' classs to the element that was clicked
    elem.classList.add('current');
}

$(function(){
     $('form').on('submit', function(e){
         e.preventDefault();
         $.ajax({
             url: $(this).attr('action'),
             method: $(this).attr('method'),
             success: function(data){ $('#target').html(data) }
         });
     });
});

 // arrRemovedElements =  document.getElementsByClassName("selected"+i );
 // for each element  => id = x
 //   document.getElementById("x").innerHTML = ""