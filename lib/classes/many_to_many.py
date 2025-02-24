class Author:
    def __init__(self, name):
        # Ensure the name is a non-empty string
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise Exception("Author name is immutable")

    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def topic_areas(self):
        topics = set([article.magazine.category for article in self._articles])
        return list(topics) if self._articles else None


class Magazine:
    def __init__(self, name, category):
        # Ensure the name is a string between 2 and 16 characters, and category is a non-empty string
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be a string with length between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Magazine name must be a string")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set([article.author for article in self._articles]))

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        # Return authors who have contributed more than 2 articles
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1

        # Return None if no authors contributed more than 2 articles
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None


class Article:
    all = []

    def __init__(self, author, magazine, title):
        # Validate title length and type
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")
        self.author = author
        self.magazine = magazine
        self.title = title
        magazine._articles.append(self)
        author._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self._magazine = value



