from django.shortcuts import render, redirect
from chemicalwords import phrase_to_chemical


def get_words(request):
    phrase = request.GET.get("phrase")

    if phrase:
        phrase = phrase.lower().strip()
        long_string = "".join([i ["symbol"] for i in phrase_to_chemical(phrase.replace(' ', ''))])
        long_made_of = phrase_to_chemical(phrase.replace(' ', ''))
        seperate_words = [
            phrase_to_chemical(word) for word in phrase.split(' ')
        ]
        if len(seperate_words) == 1 and long_string == seperate_words[0]:
            seperate_words = []

        return render(request, 'words/converted.html',
            {
                'original': phrase,
                "long_string": long_string,
                "long_made_of": long_made_of,
                'seperate_words': seperate_words
            })
    else:
        return render(request, 'words/input.html')

