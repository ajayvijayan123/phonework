from django.shortcuts import render,get_object_or_404,redirect
from.models import phonedetails
# Create your views here.

def home(request):
    return render(request,"phone.html")
def addphone(request):
    responseDic = {}
    try:
        if request.method == 'POST':
            Name = request.POST.get('name')
            Phone = request.POST.get('phone')
            print(f"Received Name: {Name}, Phone: {Phone}")  # Debugging line

            # Check if the phone entry already exists
            phnlist = phonedetails.objects.filter(name=Name)
            if phnlist.exists():
                responseDic["key"] = "Already exists"
            else:
                # Add the new phone entry
                phn = phonedetails(name=Name, phone=Phone)
                phn.save()
                responseDic["key"] = "Phone Number is added"
        
        # Render the response with the context
        return render(request, "phone.html", responseDic)
    except Exception as e:
        responseDic["key"] = f"An error occurred: {str(e)}"
        return render(request, "phone.html", responseDic)
def display(request):
    phndis= phonedetails.objects.all()
    return render(request,"phone.html",{'phn':phndis})

def delete(request):
    key1 = ""  # Initialize key1 to store messages
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            phndel = phonedetails.objects.filter(name=name)
            if phndel.exists():
                phndel.delete()
                key1 = "Deleted"
            else:
                key1 = "Name not found"
        except Exception as e:
            print(f"Error deleting contact: {e}")
            key1 = "Not Deleted"
    
    return render(request, "phone.html", {'key1': key1})


def update(request):
    key2 = ""  # Initialize key2 to store messages
    if request.method == 'POST':
        oldname = request.POST.get("oldname")
        newname = request.POST.get('newname')
        
        try:
            phndel = phonedetails.objects.filter(name=oldname)
            if phndel.exists():
                phndel.update(name=newname)
                key2 = "Updated"
            else:
                key2 = "Old name not found"
        except Exception as e:
            print(f"Error updating contact: {e}")
            key2 = "Not Updated"
    
    return render(request, "phone.html", {'key2': key2})
