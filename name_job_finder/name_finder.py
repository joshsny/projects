# Imports
import nltk
from nltk.tag.stanford import StanfordNERTagger # Stanford CoreNLP NER 
from nltk.tokenize import word_tokenize
from find_job_titles import FinderAcora # Job Title Dictionary

finder=FinderAcora() # This takes a while to load
st = StanfordNERTagger('/Users/js/GitHub/dependencies/nlp/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz',
					   '/Users/js/GitHub/dependencies/nlp/stanford-ner-2018-10-16/stanford-ner.jar',
					   encoding='utf-8') # Load NER tagger


# Finds job(s) in the string using a dictionary
def findJobs(text):
    text = ' '.join([word.title() if word.islower() else word for word in text.split()]) # Capitalise words for dictionary lookup

    try:
        jobTitles = finder.findall(text) # List of matched titles in the dictionary of job titles
    except:
        jobTitles = [] # Handle the runtime error produced when no match is found in the dictionary

    jobs = []
    for job in jobTitles:
        jobs.append(job.match)
    return jobs

# Finds name(s) in the string
def findNames(text):
    tokenizedText = word_tokenize(text) # Tokenize the input string for the Stanford Tagger
    taggedText = st.tag(tokenizedText)

    entities = {}

    tags = list(set([x[1] for x in taggedText]))

    for tag in tags: # Create key in dictionary enitities for each tag
        entities[tag] = []

    # fullEntity is used to store the current entity in its entirety (e.g Joshua Snyder, instead of ['Joshua', 'Snyder'])
    fullEntity = taggedText[0][0] # Initialise as the first word of the first entity

    for i in range(0,len(taggedText)-1):
        currentTag = taggedText[i][1]
        nextEnt = taggedText[i+1][0]
        nextTag = taggedText[i+1][1]
        if currentTag == nextTag:
            fullEntity = fullEntity + " " + nextEnt
        else:
            entities[currentTag].append(fullEntity)
            fullEntity = nextEnt

    entities[currentTag].append(fullEntity) # Append the final entity

    result = entities["PERSON"] if "PERSON" in entities else []

    return result

# Gives description
def jobDescription(text):
    names = findNames(text)
    jobs = findJobs(text)

    if (len(names) > 1) or (len(jobs) > 1):
        return "Multiple names/jobs found in text \nNames: " + str(names) +  "\nJobs: " + str(jobs)
    elif (len(names) == 0) and (len(jobs) == 0):
        return "Neither a name or job was found"
    elif (len(names) == 1) and (len(jobs) == 0):
         return "Name: " + str(names[0]) + "\nJob: Unknown"
    elif (len(names) == 0) and (len(jobs) == 1):
        return "Name: Unknown\nJob: " + str(jobs[0])
    else:
        return "Name: " + str(names[0]) +  "\nJob: " + str(jobs[0])

# Input Text
def getUserInput():
    inputText = input("Enter string for name/job title matching:\n")
    print(jobDescription(inputText))
    response = input("Would you like to try another string? (y/n): ")
    if response == "y":
        getUserInput()
    return None


getUserInput()