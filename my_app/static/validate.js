  var res = false;
  var form = $('#form1');
  var flight_error = true;
  var airlines_error = true;
  var des_error = true;
  var airplane_error = true;
  var dep_error = true;
  var arr_error = true;
  var cost_error = true;

    //-----Flight Number-----//
$('.form_field_Flight_Number').change(function(){
    var flight_number = form.find('#id_flight_number').val();
    flight_error = true;
    var error_field = form.find('#error_Flight_Number');
    var error_element = document.getElementById("error_Flight_Number");

    //-----!!-----//
    if (flight_number.length < 3) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите не менее 3 символов.');
        return;
    }
    else if (/^[a-zA-Z1-9]+$/.test(flight_number) === false) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите латиницу');
        return;
    }
    else {
        error_element.style.color="green";
        error_field.text('Верно!');
        flight_error = false;
    }
    //-----!!-----//
})

   //-----Airlines-----//
$('.form_field_Airlines').change(function(){
    var flight_number = form.find('#id_airlines').val();
    airlines_error = true;
    var error_field = form.find('#error_Airlines');
    var error_element = document.getElementById("error_Airlines");

    //-----!!-----//
    if (flight_number.length < 4) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите не менее 4 символов.');
        return;
    }

    else {
        error_element.style.color="green";
        error_field.text('Верно!');
        airlines_error = false;
    }
    //-----!!-----//
})

   //-----Desrc-----//
$('.form_field_Description').change(function(){
    var flight_number = form.find('#id_description').val();
    des_error = true;
    var error_field = form.find('#error_Description');
    var error_element = document.getElementById("error_Description");

    //-----!!-----//
    if (flight_number.length < 10) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите не менее 10 символов.');
        return;
    }
    else {
        error_element.style.color="green";
        error_field.text('Верно!');
        des_error = false;
    }
    //-----!!-----//
})

   //-----Airplane-----//
$('.form_field_Airplane').change(function(){
    var flight_number = form.find('#id_airplane').val();
    airplane_error = true;
    var error_field = form.find('#error_Airplane');
    var error_element = document.getElementById("error_Airplane");

    //-----!!-----//
    if (flight_number.length < 5) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите не менее 5 символов.');
        return;
    }
    else if (/^[a-zA-Z0-9]+$/.test(flight_number) === false) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите латиницу');
        return;
    }
    else {
        error_element.style.color="green";
        error_field.text('Верно!');
        airplane_error = false;
    }
    //-----!!-----//
})

  //-----Dep Air-----//
$('.form_field_Dep_Airport').change(function(){
    var flight_number = form.find('#id_departure_airport').val();

    var error_field = form.find('#error_Dep_Airport');
    var error_element = document.getElementById("error_Dep_Airport");

    //-----!!-----//
    if (flight_number.length != 3) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите 3 символа.');
        dep_error = true;
        return;

    }
    else if (/^[a-zA-Z1-9]+$/.test(flight_number) === false) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите латиницу');
        dep_error = true;
        return;
    }
    else {
        error_element.style.color="green";
        error_field.text('Верно!');
        dep_error = false;
    }
    //-----!!-----//
})

   //-----Arr Air-----//
$('.form_field_Arr_Airport').change(function(){
    var flight_number = form.find('#id_arrival_airport').val();

    var error_field = form.find('#error_Arr_Airport');
    var error_element = document.getElementById("error_Arr_Airport");

    //-----!!-----//
    if (flight_number.length != 3) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите 3 символа.');
        arr_error = true;
        return;
    }
    else if (/^[a-zA-Z1-9]+$/.test(flight_number) === false) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите латиницу');
        arr_error = true;
        return;
    }
    else {
        error_element.style.color="green";
        error_field.text('Верно!');
        arr_error = false;
    }
    //-----!!-----//
})

     //-----Cost-----//
$('.form_field_Cost').change(function(){
    var flight_number = form.find('#id_cost').val();

    var error_field = form.find('#error_Cost');
    var error_element = document.getElementById("error_Cost");

    //-----!!-----//
    if (flight_number.length < 3) {
        error_element.style.color="red";
        error_field.text('Ошибка! Введите не менее 3 символов.');
        cost_error = true;
        return;
    }
    else {
        error_element.style.color="green";
        error_field.text('Верно!');
        cost_error = false;
    }
    //-----!!-----//
})



$('#form_add').click(function(){
    var error_field = $('#main_error');
    if(flight_error == false && airlines_error == false &&
        airplane_error == false && des_error == false &&
        dep_error == false && arr_error == false && cost_error == false) {
        form.submit();
    }
    else {
        error_field.text('Ошибка! Заполните форму верно.');
    }
})


$(document).ready(function () {

})