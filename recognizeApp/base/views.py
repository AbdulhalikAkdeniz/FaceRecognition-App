from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage
import os
import yuztanima
import delete_uploads
import time

# Create your views here.

def index(request):

    return render(request,'index.html')

def run_script(request):

    #yuztanima.main()
    #if yuztanima.main() == 1:
        #print("WWXX")
        #return render(request, 'page2.html')

    return render(request,'index.html')


def upload_view(request):
    delete_uploads.main()
    time.sleep(1)

    fs = FileSystemStorage()
    upload_directory_images = 'uploaded_images/'  # Dosyaların kaydedileceği klasör
    upload_directory_videos = 'uploaded_videos/'
    # Klasör yoksa oluştur
    if not os.path.exists(upload_directory_images):
        os.makedirs(upload_directory_images)
    
    if not os.path.exists(upload_directory_videos):
        os.makedirs(upload_directory_videos)

    photos = request.FILES.getlist('photos')
    video = request.FILES.get('video')

    # Fotoğrafları kaydet
    for photo in photos:
        filename = fs.save(os.path.join(upload_directory_images, photo.name), photo)
        file_url = fs.url(filename)

    # Videoyu kaydet
    if video:
        #filename = fs.save(os.path.join(upload_directory_videos, video.name), video)
        filename = fs.save(os.path.join(upload_directory_videos, 'video.mp4'), video)
        file_url = fs.url(filename)
        print(video.name)

    #yuztanima.main()
    if yuztanima.main() == 1:
        print("finished")
        return render(request, 'page2.html')

    print("WWQ")
    return render(request,'index.html')


