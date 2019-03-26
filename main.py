import requests
import json


def search(search):
    # Here we define our query as a multi-line string
    query = '''
        query ($page: Int, $perPage: Int, $search: String, $mediaType: MediaType) {
          Page(page: $page, perPage: $perPage) {
            pageInfo {
              total
              currentPage
              lastPage
              hasNextPage
              perPage
            }
            media(search: $search, type: $mediaType) {
              id
              title {
                romaji
                english
              }
              genres
            }
          }
        }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        "search": search,
        "page": 1,
        "perPage": 10,
        "mediaType": "ANIME"
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})

    text_out = response.text

    with open('out.json', 'w') as out_file:
        out_file.write(text_out)


def getVars():
    return input("What do you want to search for?: ")


if __name__ == '__main__':
    search(getVars())
