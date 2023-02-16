// // $(document).ready(function(){
// //     if($('#result') != null){
// //         Read();
// //     }
// //     $('#create').on('click', function(){
// //         $firstname = $('#firstname').val();
// //         $lastname = $('#lastname').val();
  
// //         if($firstname == "" || $lastname == ""){
// //             alert("Please complete the required field");
// //         }else{
// //             $.ajax({
// //                 url: 'create/',
// //                 type: 'POST',
// //                 data: {
// //                     firstname: $firstname,
// //                     lastname: $lastname,
// //                     csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
// //                 },
// //                 success: function(){
// //                     Read();
// //                     $('#firstname').val('');
// //                     $('#lastname').val('');
// //                     alert("New Member Successfully Added");
// //                 }
// //             });
// //         }
// //     });
  
// //     $(document).on('click', '.edit', function(){
// //         $id = $(this).attr('name');
// //         window.location = "edit/" + $id;
// //     });
  
// //     $('#update').on('click', function(){
// //         $firstname = $('#firstname').val();
// //         $lastname = $('#lastname').val();
  
// //         if($firstname == "" || $lastname == ""){
// //             alert("Please complete the required field");
// //         }else{
// //             $id = $('#member_id').val();
// //             $.ajax({
// //                 url: 'update/' + $id,
// //                 type: 'POST',
// //                 data: {
// //                     firstname: $firstname,
// //                     lastname: $lastname,
// //                     csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
// //                 },
// //                 success: function(){
// //                     window.location = '/';
// //                     alert('Updated!');
// //                 }
// //             });
// //         }
  
// //     });
  
// //     $(document).on('click', '.delete', function(){
// //         $id = $(this).attr('name');
// //         $.ajax({
// //             url: 'delete/' + $id,
// //             type: 'POST',
// //             data: {
// //                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
// //             },
// //             success: function(){
// //                 Read();
// //                 alert("Deleted!");
// //             }
// //         });
// //     });
  
// // });
  
// // function Read(){
// //     $.ajax({
// //         url: 'read/',
// //         type: 'POST',
// //         async: false,
// //         data:{
// //             res: 1,
// //             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
// //         },
// //         success: function(response){
// //             $('#result').html(response);
// //         }
// //     });
// // }




// $(document).ready(function() {
//     /*------------------------------------------
//     --------------------------------------------
//     Post Listing Page 
//     --------------------------------------------
//     --------------------------------------------*/
//     var table = $('.data-table').DataTable({
//         processing: true,
//         serverSide: false,
//         columnDefs: [
//             {
//                 "render": function ( data, type, row ) {
//                     var btn = '';

//                     btn = btn + " <button class='btn btn-primary editPost' data-pk='" + row.pk + "'>" + '<i class="fa fa-pencil"></i>' + "</button>";
//                     btn = btn + " <button class='btn btn-danger deletePost' data-action='post/" + row.pk + "/delete' data-pk='" + row.pk + "'>" + '<i class="fa fa-trash"></i>' + "</button>";

//                     return btn;
//                 },
//                 "targets": 3
//             }
//         ],
//         ajax: {
//             url: "{% url 'load_data' %}",
//             dataSrc: "",
//         },
//         columns: [
//             { data: "pk" },
//             { data: "fields.title" },
//             { data: "fields.description" },
//         ]
//     });

//     /*------------------------------------------
//     --------------------------------------------
//     Click to Button
//     --------------------------------------------
//     --------------------------------------------*/
//     $('#createNewPost').click(function () {
//         $('#saveBtn').val("Create Post");
//         $('#post_id').val('');
//         $('#postForm').trigger("reset");
//         $('#modelHeading').html("Create New Post");
//         $('#ajaxModel').modal('show');
//     });
    
//     /*------------------------------------------
//     --------------------------------------------
//     Click to Edit Button
//     --------------------------------------------
//     --------------------------------------------*/
//     $('body').on('click', '.editPost', function () {
//         var post_id = $(this).data('pk');
//         $.get("post" +'/' + post_id +'/edit/', function (data) {
//             $('#modelHeading').html("Edit Post");
//             $('#saveBtn').val("edit-post");
//             $('#ajaxModel').modal('show');
//             $('#post_id').val(data.id);
//             $('#title').val(data.title);
//             $('#description').val(data.description);
//         })
//     });
    
//     /*------------------------------------------
//     --------------------------------------------
//     Print Error Msg 
//     --------------------------------------------
//     --------------------------------------------*/
//     function printErrorMsg(msg) {
//         $('.error-msg').find('ul').html('');
//         $('.error-msg').css('display','block');
//         $.each( msg, function( key, value ) {
//             $(".error-msg").find("ul").append('<li>'+value+'</li>');
//         });
//     }

//     /*------------------------------------------
//     --------------------------------------------
//     Create Post Code
//     --------------------------------------------
//     --------------------------------------------*/
//     $('#saveBtn').click(function (e) {
//         e.preventDefault();
//         $(this).html('Sending..');
        
//         $.ajax({
//             data: $('#postForm').serialize(),
//             url: "{% url 'post_store' %}",
//             type: "POST",
//             dataType: 'json',
//             success: function (data) {
//                 if ($.isEmptyObject(data.error)) {
//                     $("input[name='title']").val('');
//                     $("input[name='description']").val('');
//                     $('#ajaxModel').modal('hide');
//                     $('.success-msg').css('display','block');
//                     $('.success-msg').text(data.message);
//                 }else{
//                     printErrorMsg(data.error)
//                 }
//                 $('#postForm').trigger("reset");
//                 table.ajax.reload();
            
//             },
//             error: function (data) {
//                 $('#saveBtn').html('Save Changes');
//             }
//         });
//     });
    
//     /*------------------------------------------
//     --------------------------------------------
//     Delete Post Code
//     --------------------------------------------
//     --------------------------------------------*/
//     $("body").on("click",".deletePost",function(){
//         var current_object = $(this);
//         swal({
//             title: "Are you sure?",
//             text: "You will not be able to recover this imaginary file!",
//             type: "error",
//             showCancelButton: true,
//             dangerMode: true,
//             cancelButtonClass: '#DD6B55',
//             confirmButtonColor: '#dc3545',
//             confirmButtonText: 'Delete!',
//         },function (result) {
//             if (result) {
//                 var action = current_object.attr('data-action');
//                 var token = $("input[name=csrfmiddlewaretoken]").val();
//                 var id = current_object.attr('data-pk');

//                 $('body').html("<form class='form-inline remove-form' method='post' action='"+action+"'></form>");
//                 $('body').find('.remove-form').append('<input name="_method" type="hidden" value="delete">');
//                 $('body').find('.remove-form').append('<input name="csrfmiddlewaretoken" type="hidden" value="'+token+'">');
//                 $('body').find('.remove-form').append('<input name="id" type="hidden" value="'+id+'">');
//                 $('body').find('.remove-form').submit();
//             }
//         });
//     });
// });






