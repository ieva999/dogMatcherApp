function getSurveyData()
{
  $(document).ready

  var grooming=$('input[name=grooming]:checked').val()
  var homesize=$('input[name=homesize]:checked').val()
  var beingalone=$('input[name=beingalone]:checked').val()
  var dogsize=$('input[name=dogsize]:checked').val()
  var exercise=$('input[name=exercise]:checked').val()
  var family=$('input[name=family]:checked').val()

  document.write(exercise);


  var posturl=someUrlCorrespondingToaView;

  $('li').click(function(){
    values=[1,2];

    $.ajax({

      url:posturl,
      type:'POST',
      data:{'grooming':grooming, 'homesize':homesize, 'beingalone':beingalone, 'dogsize':dogsize, 'exercise':exercise, 'family':family},
      traditional:true,
      dataType:'html',

      success:function(result){
        $('#ingredients').append(result);
      }

    });


  });
}
