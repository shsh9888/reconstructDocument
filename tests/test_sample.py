import subprocess
import os


def textCompare(fl1,fl2):
    file1 = open(fl1, 'r')
    file2 = open(fl2, 'r')
    lines1=file1.readlines()
    lines2=file2.readlines()
    file1.close()
    file2.close()
    if lines1 == lines2:
        return True 
    else:
        return False
    

# Missing the lexicon path
def test_1():
    result = subprocess.Popen(['reconstruct-document', '--document', 'files/input.txt', '--output', 'files/output.txt'],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = result.communicate()[1]
    if "required: --lexicon" in str(output):
        assert True
    else:
        assert False

# Missing the document path
def test_2():
    result = subprocess.Popen(['reconstruct-document', '--lexicon', 'files/lex.txt', '--output', 'files/output.txt'],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = result.communicate()[1]
    if "required: --document" in str(output):
        assert True
    else:
        assert False

# Missing the output path
def test_3():
    result = subprocess.Popen(['reconstruct-document', '--lexicon', 'files/lex.txt', '--document', 'files/input.txt'],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = result.communicate()[1]
    if "required: --output" in str(output):
        assert True
    else:
        assert False

# Missing all the arguments
def test_4():
    result = subprocess.Popen(
        ['reconstruct-document'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = result.communicate()[1]
    if "required: --lexicon, --document, --output" in str(output):
        assert True
    else:
        assert False

#File do not exist
def test_5():
    result = subprocess.Popen(['reconstruct-document', '--lexicon','files/nofile.txt','--document', 'files/input.txt', '--output', 'files/output.txt'],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    #print(result.communicate())
    output = result.communicate()
    if "File path files/nofile.txt does not exist" in str(output):
        assert True
    else:
        assert False


##Successful runs
def test_6():
    os.system('reconstruct-document --lexicon files/lex.txt --document  files/input.txt --output files/output.txt')
    
    if textCompare('files/output.txt', 'files/true_output.txt'):
        assert True
    else:
        assert False

def test_7():
    os.system('reconstruct-document --lexicon files/lex1.txt --document  files/doc1.txt --output files/output1.txt')

    if textCompare('files/output1.txt', 'files/true_output1.txt'):
        assert True
    else:
        assert False

def test_8():
    os.system('reconstruct-document --lexicon files/lex2.txt --document  files/doc2.txt --output files/output2.txt')

    if textCompare('files/output2.txt', 'files/true_output2.txt'):
        assert True
    else:
        assert False


def test_clean():
    os.system("rm files/output*")
    assert True