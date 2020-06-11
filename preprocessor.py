from bs4 import BeautifulSoup
import time

t0 = time.time()
with open('bigFile.xml') as raw_file:
    entire_file_soup = BeautifulSoup(raw_file, 'lxml')
    debateBody_tag = entire_file_soup.debatebody
    data = []

    for debateSection in debateBody_tag.children:
        day_of_debates_soup = BeautifulSoup(str(debateSection), 'lxml')
        day = day_of_debates_soup.heading
        if day:
            day = "".join(day)
        for inside in day_of_debates_soup.children:
            specific_debate_soup = BeautifulSoup(str(inside), 'lxml')
            for tag in specific_debate_soup.debatesection.contents:
                if str(tag.name) == 'debatesection':
                    title = "".join(tag.contents[1])
                    content = str(tag.find_all('p'))
                    tupleofshit = (day,title,content)
                    data.append(tupleofshit)
t1 = time.time()
total = t1-t0
print(total)