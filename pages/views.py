from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
def home(request):
    context = {
        'title' : 'Home',
        'features' : [
            'DJango', 
            'Templates', 
            'Static Files'
        ]
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', { 'title':'About' })

def hello(request, name):
    return render(request, 'hello.html', {'name':name})


def gallery(request):
    images = ['img1.jpg', 'img2.jpg', 'img3.jpg']
    return render(request, 'gallery.html', {'images': images})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)

ANNOUNCEMENTS = {
    "appstore": {
        "title": "New App Store Release (v2.0)",
        "date": "Sept 20, 2025",
        "version": "2.0",
        "short": "Our latest app update is now available on the App Store!",
        "long": """This release focuses on delivering a smoother user experience,
                   with optimized performance, a refreshed interface, and improved
                   multi-device compatibility. We've also included bug fixes and
                   stability updates.

                   In version 2.0, we’ve introduced faster loading times, 
                   an upgraded navigation system, and a modernized design 
                   that follows the latest accessibility standards. 
                   Notifications are now more reliable, ensuring you stay updated 
                   with the latest announcements and system alerts. 

                   This version has also been optimized for tablets and larger screens, 
                   providing a more seamless multi-device experience. 
                   Security protocols were upgraded to safeguard user data 
                   while ensuring smooth connectivity across networks."""
    },
    "maintenance": {
        "title": "Scheduled Maintenance",
        "date": "Sept 20, 2025",
        "version": "N/A",
        "short": "The system will undergo maintenance at midnight.",
        "long": """We will be carrying out essential updates to improve overall
                   stability, security, and performance. Expected downtime is
                   approximately 2 hours.

                   During this maintenance window, certain features such as 
                   user login, announcements, and gallery browsing may be 
                   temporarily unavailable. We strongly advise all users 
                   to save their progress and log out prior to the scheduled 
                   downtime to avoid disruptions.

                   Our technical team will also be deploying critical 
                   security patches, improving database efficiency, 
                   and preparing the system for upcoming feature releases. 
                   Once the maintenance is complete, users can expect a 
                   smoother, more secure, and more responsive platform."""
    },
}


def details(request, slug):
    announcement = ANNOUNCEMENTS.get(slug)
    if not announcement:
        raise Http404("Announcement not found")
    return render(request, "list.html", {"announcement": announcement})

def announcements(request):
    return render(request, 'announcements.html', {"announcements": ANNOUNCEMENTS})