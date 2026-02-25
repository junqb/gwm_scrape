


def return_page_number(soup):
    # 1. Find the "next" button
    next_button = soup.find('a', class_='paginator-next')

    # 2. Get the text immediately before it
    # .previous_sibling captures the " Page 1 of 8 " text node
    pagination_text = next_button.previous_sibling.strip()

    # 3. Extract the last number
    # Split the string ["Page", "1", "of", "8"] and take the last element
    total_pages = int(pagination_text.split()[-1])

    return total_pages

if __name__ == "__main__":
    pass