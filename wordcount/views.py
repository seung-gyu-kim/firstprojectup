from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    fullText = request.GET['fulltext']
    wordList = fullText.split()
    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            # Increase
            wordDictionary[word] += 1
        else:
            # add to the dictionary
            wordDictionary[word] = 1   

    return render(request, 'wordcount/count.html', {'fulltext': fullText, 'total': len(wordList), 'dictionary': wordDictionary.items() })
