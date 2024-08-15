import requests
from bs4 import BeautifulSoup

def fetch_python_solution_from_algo_monster(problem_number):
    # Construct the URL using the problem number
    algo_monster_url = f"https://algo.monster/liteproblems/{problem_number}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Fetch the Algo.Monster page content
    response = requests.get(algo_monster_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page, status code: {response.status_code}")
        return None
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the <code class="language-python"> element
    python_code_element = soup.find('code', {'class': 'language-python'})
    if not python_code_element:
        print("Python code element not found.")
        return None
    
    # Extract the text content from the code element
    code_text = python_code_element.get_text()
    
    # Return the code text
    return code_text


#if __name__ == "__main__":
#    problem_number = "860"  # Replace with the actual problem number
#    python_solution = fetch_python_solution_from_algo_monster(problem_number)
#    if python_solution:
#        print(f"Python Solution Code:\n{python_solution}")
#    else:
#        print("No solution found or could not retrieve the solution.")
