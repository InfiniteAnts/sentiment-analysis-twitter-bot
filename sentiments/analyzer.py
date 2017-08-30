import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        #"""Initialize Analyzer."""
        
        # Creating an empty list to store positve words
        self.positives = []
        with open (positives) as lines:
            for line in lines:
                
                # Ignore lines starting with ';' and blank lines
                if not (line.startswith(';')):
                    
                    # Append the word to the list and remove any whitespace
                    self.positives.append(line.strip())
                    
        # Creating an empty list to store negative words
        self.negatives = []
        with open (negatives) as lines:
            for line in lines:
                
                # Ignore lines starting with ';' and blank lines
                if not (line.startswith(';')):
                    
                    # Append the word to the list and remove any whitespace
                    self.negatives.append(line.strip())
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
        # If positive word return positive score
        if text.lower() in self.positives:
            return 1
        
        # If negative word return negative score    
        elif text.lower() in self.negatives:
            return -1
            
        # Else return 0    
        else:
            return 0
