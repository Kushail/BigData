from bs4 import BeautifulSoup

with open('bigFile.xml') as raw_file:
    soup = BeautifulSoup(raw_file, 'lxml')
    debateBody = soup.debatebody   # tag object, its the parent tag of all debatesections called debatebody
    #results = debateBody.find_all('debatesection', recursive = False) # returns array of each parent debatesection
    

    output2 = open("output2.xml", "w")
    
    #for child in results
    for debateSection in results[0].children
        print(debateSection)
        output.write(str(debateSection))






    