from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def result(request):
    text = request.POST["text"]
    count = len(text)
    without_space = len(text.replace(" ", ""))
    words = text.split()
    word_count = len(words)
    
    word_dict = {}
    for i in words:
        if i in word_dict.keys():
            word_dict[i] += 1
        else:
            word_dict[i] = 1

    print(word_dict)

    context = {
    "count" : count,
    "word_count" : word_count,
    "without_space" : without_space,
    "word_dict" : word_dict.items()
    }

    return render(request, 'result.html', context)