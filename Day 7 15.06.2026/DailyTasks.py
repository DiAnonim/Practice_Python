'''
Help the bookseller !

A bookseller has lots of books classified in 26 categories labeled A, B, C, ..., Z. 
Each book has a code of at least 3 characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code is followed by a space and by a positive integer,
which indicates the quantity of books of this code in stock.

Task
You will receive the bookseller's stocklist and a list of categories.
Your task is to find the total number of books in the bookseller's stocklist,
with the category codes in the list of categories. Note: the codes are in the same order in both lists.

result as a string described in the example below, or as a list of pairs (Haskell/Clojure/Racket/Prolog).

If any of the input lists is empty, return an empty string, or an empty array/list (Clojure/Racket/Prolog).

'''

def stock_list(stocklist, categories):
    if not stocklist or not categories: return ""
    
    result_data = {category: 0 for category in categories}
    
    for books in stocklist:
        
        books_category = books[0]
        
        if books_category in result_data:
            space_index = books.find(" ")
            result_data[books_category] += int(books[space_index + 1:])
    
    result_parts = []
    
    for category in categories:
        cnt_books = result_data.get(category, 0)
        result_parts.append( f"({category} : {cnt_books})" )
    
    return " - ".join(result_parts)

# res = (A : 20) - (B : 114) - (C : 50) - (W : 0)
b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
c = ["A", "B", "C", "W"]
print(stock_list(b, c))