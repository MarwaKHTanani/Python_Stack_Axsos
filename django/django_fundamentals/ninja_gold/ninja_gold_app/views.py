from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    context = {
        'gold': request.session['gold'],
        'activities': request.session['activities']
    }
    return render(request, 'index.html', context)

def process_money(request):
    if request.method == 'POST':
        building = request.POST['building']
        if building == 'farm':
            gold_earned = random.randint(10, 20)
        elif building == 'cave':
            gold_earned = random.randint(10, 20)
        elif building == 'house':
            gold_earned = random.randint(10, 20)
        elif building == 'quest':
            gold_earned = random.randint(-50, 50)
        
        current_time = datetime.now().strftime("%B-%d-%Y %I:%M:%p")

        request.session['gold'] += gold_earned
        activity = f"you entered a{building} and earned {gold_earned} gold. ({current_time})"
        if gold_earned < 0:
            activity = f"you failed a quest and lost {abs(gold_earned)} gold.Ouch. ({current_time})"
        activities = request.session['activities']
        activities.append(activity)
        request.session['activities'] = activities

    return redirect('/')

    