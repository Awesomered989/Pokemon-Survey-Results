var can = document.getElementById("mycanvas");
var ctx = can.getContext("2d");
console.log(results);

var ranks = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th"]

function get_rank(r){
    if (r.toString().slice(-1)==1 && r.toString().slice(-2)!=11){
        return r+"st";
    }
    else if (r.toString().slice(-1)==2 && r.toString().slice(-2)!=12){
        return r+"nd";
    }
    else if (r.toString().slice(-1)==3 && r.toString().slice(-2)!=13){
        return r+"rd";
    }
    else{
        return r+"th";
    }
}

$(document).ready(function(){
    var question="Favourite Type";
    var options=results[question];
    var optionL=options.length;
    console.log(options)

    //ctx.fillStyle = "red";
    //ctx.fillRect(0, 0, 100, 100);
  

    options.forEach((item, index) => {
        console.log(item, index, get_rank(index+1),item.toLowerCase());
        rank=get_rank(index+1);

        var img = new Image; img.src="images/"+item.toLowerCase()+".png";
        console.log(img);
        ctx.drawImage(img,10,10);

        var width = Math.floor(can.width/optionL);
        var height = Math.floor((can.height)*((optionL-index)/optionL));

        var x = index*width;
        var y = can.height-Math.floor((can.height-50)*((optionL-index)/optionL));
        
        ctx.fillStyle = "red";
        ctx.fillRect(x, y, width, height);
        ctx.strokeRect(x, y, width, height)
    });
});