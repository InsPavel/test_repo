$("#selectAll").click(function(){
        $("input[type=checkbox]").prop('checked', $(this).prop('checked'));

});

function showButton() {
    let buttonDelete = document.getElementById("deleteButton");
    let checked_true = $("input[type=checkbox]").prop('checked');
    if (checked_true) {
        buttonDelete.style.display = "inline-block"
    } else {
        buttonDelete.style.display = "none"
    }
}

function showButtonDelete() {
    let buttonDelete = document.getElementById("deleteButton");
    let length = document.querySelectorAll('input[type="checkbox"]:checked').length;
    if (length > 0) {
        buttonDelete.style.display = "inline-block"
    } else {
        buttonDelete.style.display = "none"
    }
}


function showFormEdit(pk) {
    let href = '/issue/' + pk + '/edit/';
    $.ajax({
        type: 'GET',
        url: href,
        success: function (data) {
            $('#foo_modal').find('.modal-body').html(data);
            $('#foo_modal').modal('show');
        },
    });
}


function hideFormEdit(){
    $('#foo_modal').modal('hide');
}


function showDelete() {
    var checkedValue = [];
    var inputElements = document.getElementsByClassName('checkBox');
    for(var i=0; inputElements[i]; i++){
          if(inputElements[i].checked){
               checkedValue.push(inputElements[i].value);
          }
    }
    let issue_pk = checkedValue.join(';');
    let href = '/issue/delete/get/';
    $.ajax({
        type: 'GET',
        url: href,
        data: {
            issue_pk: issue_pk
        },
        success: function (data) {
            $('#foo_modal').find('.modal-body').html(data);
            $('#foo_modal').modal('show');
        },
    });
}


