function add(table){
    if(table=='product'){
    productname=document.getElementById('product').value;
    subtitle=document.getElementById('subtitle').value;
    desc=document.getElementById('desc').value;
    brand=document.getElementById('brand').value;
    service=document.getElementById('service').value;
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "add?table="+product+"&product="+productname+"&subtitle="+subtitle+"&desc="+desc+"&brand="+brand+"&service="+service, true);
    xhttp.send();
}
}
console.log('hi');
function show(table){
    
}