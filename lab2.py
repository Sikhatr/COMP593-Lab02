
def main():
    student_data = {
        'full_name': 'Sisan Khatri',
        'student_id': 10284343,
        'pizza_toppings': ['PINEAPPLE', 'PEPPERONI', 'OLIVES'],
        'movies': [
            {'title': 'Interstellar', 'genre': 'Science fiction'},
            {'title': 'Five Feet Apart', 'genre': 'Romance'},

        ]
    }
    def print_student_info(data):
        name = data['full_name']
        first_name = name.split ()[0]
        student_id = data['student_id']
        print(f"My name is {name},but you can call me Miss {first_name}.")
        print(f"My student ID is {student_id}.")


    def add_pizza_toppings(data, toppings):
        pizza_toppings = data['pizza_toppings']
        pizza_toppings.extend(toppings)
        pizza_toppings.sort()
        pizza_toppings = [topping.lower() for topping in pizza_toppings]
        data["pizza_toppings"] = pizza_toppings


    def print_pizza_toppings(data):
        pizza_toppings = data['pizza_toppings']
        print("My favourite pizza toppings are:")
        for topping in pizza_toppings:
            print(f"- {topping}")


    def print_movie_genres(data):
        movies = data["movies"]
        genres = [movie['genre'] for movie in movies]
        genre_str = "," .join(genres)
        print(f"I like to watch {genre_str} movies.")



    def print_movie_titles(movies):
        titles = ', '.join([movie["title"].title() for movie in movies])
        print(f"Some of my favourite movies are {titles}!")
        


    print_student_info(student_data)
    print_pizza_toppings(student_data)
    add_pizza_toppings(student_data, ['CHICKEN', 'BACON'])
    print_pizza_toppings(student_data)
    print_movie_genres(student_data)
    print_movie_titles(student_data['movies'])


if __name__ == '__main__':
     main()    
            
