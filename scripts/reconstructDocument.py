#!/usr/bin/env python3

import os
import argparse

"""
Reconstruct the document wihtout spaces

:param input: Sentence without the spaces
:param dict:  Dictionary of words in lexicon
"""

def reconstruct_document(input, dict):
    if input in dict:
        return input

    for i in range(0, len(input)):
        prefix =  input[0:i]
        if prefix in dict:
            rest_suffix = input[i:]
            suffix = reconstruct_document(rest_suffix, dict)
            if suffix != "":
                return prefix + " " +  suffix

    return ""


"""
Testing the reconstructed document

:param content: document with spaces
:param dict:  Dictionary of words in lexicon
"""

def test(content, dict):
    content = content.replace(".", " ")
    words = content.split(" ")
    words = words[:len(words)-1]
    for word in words:
        if word not in dict:
            print(word," not there in dictionary")
    print("Test Ended")



"""
Accept and parse command line argument. 
"""
def main():
    #Read and validate the command line arguements
    ap = argparse.ArgumentParser()
    ap.add_argument( "--lexicon", required=True,
                    help="Filepath to the lexicon being used")
    ap.add_argument( "--document", required=True,
                    help="Filepath to the ruined document to reconstruct")
    ap.add_argument( "--output", required=True,
                    help="Filepath to which the reconstructed document will be written")
    args = vars(ap.parse_args())

    lexFilePath,documentPath,outputPath  = args['lexicon'] ,args['document'],args['output']

    if not os.path.isfile(lexFilePath):
        print("File path {} does not exist. Exiting...".format(lexFilePath))
        return
    if not os.path.isfile(documentPath):
        print("File path {} does not exist. Exiting...".format(documentPath))
        return

    ##Once all the validations are done.

    lexiconDictionary ={}
    documentWithSpace =""

    ##Read all the words in the lexicon and add it to dictionary

    with open(lexFilePath) as f:
        content =f.readlines()
        for word in content:
            lexiconDictionary[word.strip()] =word.strip()
        f.close()
    with open(documentPath) as f:
        doc = f.read()
        f.close()
    sentences = doc.split('.')
    ## removing  the last empty string
    sentences = sentences[:(len(sentences)-1)]

    ## Reconstruct sentence by sentence
    for sentence in sentences:
        doc = reconstruct_document(sentence, lexiconDictionary)
        if doc != None or doc != "":
            documentWithSpace = documentWithSpace + doc +"."

    #test(documentWithSpace,lexiconDictionary)

    with open(outputPath, 'a+') as f:
        f.write(documentWithSpace)
        f.close()

main()




