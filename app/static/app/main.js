console.log('hello world')
const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('image-box')
const imageForm = document.getElementById('image-form')
const confirmBtn = document.getElementById('confirm-btn')
const input = document.getElementById('id_picture')

const csrf = document.getElementsByName('csrfmiddlewaretoken')

input.addEventListener('change', () => {
  console.log('changed')
  alertBox.innerHTML = ""
  confirmBtn.classList.remove('not-visible')
  const img_data = input.files[0]
  const url = URL.createObjectURL(img_data)

  imageBox.innerHTML = `<img src="${url}" id="image" width="400px">`
  var $image = $('#image')

  var $image = $('#image');

  $image.cropper({

    aspectRatio: 16 / 16,
    crop: function(event) {
      console.log(event.detail.x);
      console.log(event.detail.y);
      console.log(event.detail.width);
      console.log(event.detail.height);
      console.log(event.detail.rotate);
      console.log(event.detail.scaleX);
      console.log(event.detail.scaleY);
    }
  });

  // Get the Cropper.js instance after initialized
  var cropper = $image.data('cropper');

  confirmBtn.addEventListener('click', ()=>{
    cropper.getCroppedCanvas().toBlob((blob) => {
        console.log('confirmed')
        const fd = new FormData();
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('picture', blob, 'my-image.png');

        $.ajax({
            type:'POST',
            url: imageForm.action,
            enctype: 'multipart/form-data',
            data: fd,
            success: function(response){
                console.log('success', response)
                alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                                        保存されました。結果を見るを押してください。
                                    </div>`
            },
            error: function(error){
                console.log('error', error)
                alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                                        保存に失敗しました。
                                    </div>`
            },
            cache: false,
            contentType: false,
            processData: false,
        })
    })
})
});



