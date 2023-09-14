from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.db.models import Q

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            info = form.save()
            # Redirect or do something else
            messages.success(request, 'New fresher added sucessfully')
            return redirect('home')
    else:
        form = InfoForm()
        return render(request, 'dlcf/home.html', {'form': form})

    return render(request, 'dlcf/home.html', {'form': form})

def all_freshers(request):
    members = Info.objects.all()
    return render(request, 'dlcf/freshers.html', {'members':members})



def update(request, id):
    fresher = Info.objects.get(id=id)
    form = InfoForm(instance=fresher)

    if request.method == 'POST':
        form = InfoForm(request.POST, instance=fresher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fresher info updated')
            return redirect('fresher-info', id=fresher.id)
        else:
            messages.error(request, 'Invalid credentials')
    
    # Move this return statement out of the 'else' block
    return render(request, 'dlcf/update-fresher.html', {'form': form})



def fresher_info(request, id):
    try:
        member = Info.objects.get(id=id)
    except Info.DoesNotExist:
        messages.success(request, 'Not found')
        return redirect('freshers')
    return render(request, 'dlcf/fresher-info.html', {'member': member})



def search(request):
    if request.method == 'POST':
        # Initialize query and filter variables
        query = request.POST.get('q')
        location = request.POST.get('location')
        hostel = request.POST.get('h')

        # Get all members initially
        members = Info.objects.all()

        # Construct the filter conditions based on user input
        filter_conditions = Q()

        if query:
            filter_conditions |= Q(first_name__icontains=query) | Q(last_name__icontains=query)
            print(query)
        if location:
            filter_conditions |= Q(location__icontains=location)
            print(location)
        if hostel:
            filter_conditions |= Q(hostel__icontains=hostel)
            print(hostel)
        # Apply the filter conditions to the queryset
        if filter_conditions:
            members = members.filter(filter_conditions)
            print(filter_conditions)
        # Now you can use 'members' for further processing or return the results
        context = {
            'members': members,
        }

        print(members)

        return render(request, 'dlcf/results.html', context)

    else:
        return render(request, 'dlcf/search.html')




    # if request.method == 'POST':
    #     # Initialize query and filter variables
    #     query = request.GET.get('q')
    #     location = request.GET.get('location')
    #     hostel = request.GET.get('h')

    #     # Get all members initially
    #     members = Info.objects.all()

    #     if query and location and hostel:
    #         members = members.filter(
    #             (Q(first_name__icontains=query) | Q(last_name__icontains=query)) 
    #             & Q(hostel__icontains=hostel) & Q(location__icontains=location)
    #         )

    #     # Apply search query if provided
    #     elif query and location and hostel=="":
    #         members = members.filter(
    #             Q(first_name__icontains=query) | Q(last_name__icontains=query)
    #             & Q(location__icontains=location)
    #         )

    #     elif query and hostel and location=="":
    #         members = members.filter(location__icontains=location & Q(hostel__icontains=hostel))


    #     elif query and hostel=="" and location=="":
    #         members = members.filter((Q(first_name__icontains=query) | Q(last_name__icontains=query)))

        
    #     elif hostel and query=="" and location=="":
    #         members = members.filter(hostel__icontains=hostel)


    #     elif location and query=="" and hostel=="":
    #         members = members.filter(location__icontains=location)


    #     # Now you can use 'members' for further processing or return the results
    #     context = {
    #         'members': members,
    #     }

    #     return render(request, 'dlcf/results.html', context)

    # else:
    #     return render(request, 'dlcf/search.html') 