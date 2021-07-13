import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    total_pages = int(input('How many pages should be scrapped?: \n'))
    req_score = int(input('What is the score that you consider: \n'))
    storylinks, subtexts = [], []

    page = 1
    while page < total_pages:
        response = requests.get('https://news.ycombinator.com/news?p={0}'.format(page))
        soup = BeautifulSoup(response.text, 'html.parser')
        storylinks = storylinks + soup.select('.storylink')
        subtexts = subtexts + soup.select('.subtext')
        page+=1

    # print(subtexts[0].span.text.split(' ')[0])

    results = []
    for index, storylink in enumerate(storylinks):
        count = int(subtexts[index].span.text.split(' ')[0])   #if score is greater than hundred then we will consider that post
        if count > req_score:
            each_result = dict()
            each_result['text'] = storylink.text
            each_result['ref'] = storylink.get('href')
            each_result['count'] = count
            results.append(each_result)



    #lets sort the results in ascending order

    results = sorted(results, key = lambda x : x['count'])

    print(results)   # This will print the list of dictionaries in the sorted order based on the score
