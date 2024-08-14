import requests
from bs4 import BeautifulSoup

def fetch_daily_leetcode_problem():
    url = "https://leetcode.com/graphql/"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    query = """
    {
        activeDailyCodingChallengeQuestion {
            date
            link
            question {
                acRate
                difficulty
                questionId
                isFavor
                isPaidOnly
                status
                title
                titleSlug
                hasVideoSolution
                hasSolution
                topicTags {
                    name
                    id
                    slug
                }
                content
            }
        }
    }
    """

    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()

    if 'errors' in data:
        print("Error in response:", data['errors'])
        return None

    question = data['data']['activeDailyCodingChallengeQuestion']['question']
    title = question['title']
    link = f"https://leetcode.com/problems/{question['titleSlug']}/"
    difficulty = question['difficulty']
    ac_rate = question['acRate']
    content_html = question['content']

    soup = BeautifulSoup(content_html, 'html.parser')
    problem_description = soup.get_text()

    return {
        "title": title,
        "link": link,
        "difficulty": difficulty,
        "ac_rate": ac_rate,
        "description": problem_description
    }

daily_problem = fetch_daily_leetcode_problem()
if daily_problem:
    print(f"Today's LeetCode problem: {daily_problem['title']}")
    print(f"Difficulty: {daily_problem['difficulty']}")
    print(f"Acceptance Rate: {daily_problem['ac_rate']}%")
    print(f"Link: {daily_problem['link']}")
    print(f"Description: {daily_problem['description']}")
