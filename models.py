# создал класс а потом понял что нет необходимости
class Book():
    def __init__(self, id: int, title: str, author: str, year: int, status: str):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        if status not in ['в наличии', 'выдана']:
            raise ValueError("status должен быть 'в наличии'/'выдана'")
        self.status = status

    def __str__(self):
        return f'{self.title} {self.author} {self.year} {self.status}'
