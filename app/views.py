from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseServerError
from django.urls import reverse

from font.settings import MODEL_ROOT

from .models import Image
from .forms import ImageForm
from django.views.decorators.http import require_POST
import os
import tempfile

from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2
import requests

from django_cleanup import cleanup



def index(request):
    return render(request, 'app/index.html')

def crop(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return JsonResponse({'massage': 'works'})
    context = {'form':form}
    return render(request, 'app/crop.html', context)


def result(request):
    name = np.array(['MS ゴシック','MS 明朝','メイリオ','游ゴシック','UDデジタル教科書体'],dtype=object)

    path = 'https://res.cloudinary.com/hriscwqpd/image/upload/v1638897819/media/images/my-image.png'
    #is_file = os.path.isfile(path)

    #if is_file:
    image = imread_web(path)
    image = cv2.resize(image,dsize=(224,224))
    image = image/255.0
    test_image = (np.expand_dims(image,0))
    model = tf.keras.models.load_model(MODEL_ROOT)
    predictions = model.predict(test_image)
    predictions_sort = np.argsort(predictions[0])[::-1]
    name_sort = name[predictions_sort]
    result_sort = predictions[0][predictions_sort]
   # else:
       # print('not exit')
        #return render(request,'app/index.html')

    context = {
        'name':name_sort,
        'result':result_sort
    }
    return render(request, 'app/result.html',context)

def imread_web(url):
    # 画像をリクエストする
    res = requests.get(url)
    img = None
    # Tempfileを作成して即読み込む
    fp = tempfile.NamedTemporaryFile(dir='./', delete=False)
    fp.write(res.content)
    fp.close()
    img = cv2.imread(fp.name)
    os.remove(fp.name)
    return img
