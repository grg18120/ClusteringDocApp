#Download and import spacy
#Guide https://stackoverflow.com/questions/36835341/pip-is-not-recognized
#Error: pip : The term 'pip' is not recognized as the name of a cmdlet, function, script file, or operable program.
#1)Add pip to Environment Variables 
#    This PC -> Properties -> Advanced System Settings -> Environment Variables ->
#    on System variables clik on Path and then Edit -> New ->
#    Copy/Paste the path where pip exist (C:\Users\George Georgariou\source\repos\ClusteringDocApp\ClusteringDocApp\VirtualEnvironmentClustDoc\Scripts)
#2)pip install -U pip setuptools wheel
#3)pip install -U spacy
#
#Download trained pipelines (en_core_web_sm, el_core_news_sm)
#python -m spacy download en_core_web_sm
#python -m spacy download el_core_news_sm

import spacy
nlpEn = spacy.load('en_core_web_sm')
nlpGr = spacy.load('el_core_news_sm')