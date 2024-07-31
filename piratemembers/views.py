import random
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from .models import User

def home(request, user_id):
    user = User.objects.get(user_id=user_id)
    return render(request, 'home.html', {'user': user})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(user_id=user_id, password=password)
                request.session['user_id'] = user_id
                return redirect('home', user_id=user_id)
            except User.DoesNotExist:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    request.session.flush()
    return redirect('login')

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import random

def random_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'error': 'User not logged in'}, status=403)

    user = get_object_or_404(User, user_id=user_id)
    if user.random_used:
        return JsonResponse({
            'stamina': user.stamina,
            'heal': user.heal,
            'skill': user.skill,
            'rank': user.rank,
            'total': user.stamina + user.heal + user.skill,
            'error': 'Random already used'
        }, status=403)

    stamina = random.randint(1, 5)
    heal = random.randint(1, 5)
    skill = random.randint(1, 5)
    total = stamina + heal + skill

    ranks = {
        3: "ทาส",
        4: "เด็กฝึกหัด",
        5: "ลูกกระจ๊อก",
        6: "ช่างซ่อมเรือ",
        7: "หมอ",
        8: "คนเดินเรือ",
        9: "พลซุ่มยิง",
        10: "หน่วยต่อสู้",
        11: "มือสังหาร",
        12: "มือขวา",
        13: "รองกัปตันเรือ",
        14: "กัปตันเรือ",
        15: "กัปตันเรือ"
    }

    rank = ranks.get(total, "Unknown")

    user.stamina = stamina
    user.heal = heal
    user.skill = skill
    user.rank = rank
    user.random_used = True
    user.save()

    return JsonResponse({
        'stamina': stamina,
        'heal': heal,
        'skill': skill,
        'rank': rank,
        'total': total
    })
