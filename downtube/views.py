from django.shortcuts import render
import pafy

def youtube(request):
    if request.method=='POST':
        try:
            url=request.POST.get('url')
            # Creating Object
            video=pafy.new(url)
            return render(request,'yt_main.html',{'video':video})
            # Message for Wrong URL
        except ValueError:
            error="Please Enter a valid url!!! "
            return render(request,'yt_main.html',{'error':error})
        except:
            error="sorry! we are facing some problems :("
            return render(request,'yt_main.html',{'error':error})


    res=render(request,'yt_main.html')
    return res
    
    
