from django.shortcuts import render

def table_view(request):
    result = []
    number = None
    if request.method == "POST":
        number = int(request.POST.get('number'))
        result = [number * i for i in range(1, 11)]

    return render(request, 'tableapp/table.html', {'number': number, 'result': result})
