from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .game import Game
from .messages import INT_ERRORE_MESSAGE


def handle(request):
    if request.method == "GET":
        return render(request, "main.html")
    else:
        numbers = [(request.POST.get("numbers"))]
        error_message = []
        try:
            num = ", ".join(numbers)
            numbers_list = num.split()
            numbers_list = [int(number) for number in numbers_list]
            game = Game()
            game_result = []
            validation = game.validation(numbers_list)
            if validation:
                error_message.append(validation)
            else:
                game_result.append(game.get_result())
            context = {
                "nums": request.POST.get("nums"),
                "game_result": "".join(game_result),
                "error_message": "".join(error_message)
            }
        except ValueError:
            error_message.append(INT_ERRORE_MESSAGE)
            context = {
                "nums": request.POST.get("nums"),
                "error_message": "".join(error_message)
            }

        return render(request, 'main.html', context)
