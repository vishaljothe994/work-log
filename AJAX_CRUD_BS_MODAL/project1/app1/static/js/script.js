$(document).ready(function(){

    if($('#result') != null){
        Read();
    }
    $('#create').on('click', function(){
        $firstname = $('#firstname').val();
        $lastname = $('#lastname').val();
        let member_key = $('#member_key').val();
        console.log(member_key);
        console.log('member_key');
        if($firstname == "" || $lastname == ""){
            alert("Please complete the required field");
        }else{
            $.ajax({
                url: 'create/',
                type: 'POST',
                data: {
                    member_key:member_key,
                    firstname: $firstname,
                    lastname: $lastname,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    Read();
                    $('#firstname').val('');
                    $('#lastname').val('');
                    alert("New Member Successfully Added");
                    $(form)[0].reset();
                }
            });
        }
    });




 
    $(document).on('click', '.edit', function(){
        $senid = $(this).attr('name');
        mydata = {uid:$senid,csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()};
        $.ajax({
            url:'edit/',
            type:'post',
            data:mydata,
            success:function(data){
                console.log(data)
                $('#firstname').val(data.member.firstname);
                $('#lastname').val(data.member.lastname);
                $('#member_key').val(data.member.id);

            },
        });  
    });


    // $('#update').on('click', function(){
    //     $firstname = $('#firstname').val();
    //     $lastname = $('#lastname').val();
  
    //     if($firstname == "" || $lastname == ""){
    //         alert("Please complete the required field");
    //     }
    //     else{
    //         $id = $('#member_id').val();
    //         $.ajax({
    //             url: 'update/' + $id,
    //             type: 'POST',
    //             data: {
    //                 firstname: $firstname,
    //                 lastname: $lastname,
    //                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    //             },
    //             success: function(){
    //                 window.location = '/';
    //                 alert('Updated!');
    //             }
    //         });
    //     }
  
    // });


  
    $(document).on('click', '.delete', function(){
        $id = $(this).attr('name');
        $.ajax({
            url: 'delete/' + $id,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                Read();
                alert("Deleted!");
            }
        });
    });
  
});
  
function Read(){
    $.ajax({
        url: 'read/',
        type: 'POST',
        async: false,
        data:{
            res: 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#result').html(response);
        }
    });
}