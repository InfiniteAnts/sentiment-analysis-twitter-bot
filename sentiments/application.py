from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer

import os
import sys
import nltk

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, 100)
    if tweets == None:
        return redirect(url_for("index"))

    # TODO
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    
    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)
    
    # Importing the Tokenizer and using it
    tokenizer = nltk.tokenize.TweetTokenizer()
    
    # Number of positive, negative and neutral tweets
    positiven, negativen, neutraln = 0.0, 0.0, 0.0
    
    # analyze tweet
    for tweet in tweets:
        counter = 0
        
        # tokens contains the whole tweet split into words
        tokens = tokenizer.tokenize(tweet)
        
        # Iterating through all the words in the whole tweet
        for token in tokens:
            
            # analyze word
            score = analyzer.analyze(token)
            counter += score
            
        if counter > 0.0:
            positiven += 1
        elif counter < 0.0:
            negativen += 1
        else:
            neutraln += 1
      
        # Expressing positive, negative and neutral tweets as %      
        positive = (positiven/len(tweets)) * 100
        negative = (negativen/len(tweets)) * 100
        neutral = (neutraln/len(tweets)) * 100

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
