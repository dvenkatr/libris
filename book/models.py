from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=300, unique=True)
    def __str__(self):
        return self.name


class Award(models.Model):
    AWARD_CHOICES = (
        ('Pulitzer', 'Pulitzer'),
        ('Booker', 'Booker'),
        ('Hugo', 'Hugo')
    )
    award = models.CharField(max_length=10, choices=AWARD_CHOICES, blank=True, null=True)
    award_year = models.PositiveIntegerField(blank=True, null=True)
    def __str__(self):
        return f'{self.award}, {self.award_year}'


class Book(models.Model):
    isbn = models.CharField(max_length=20, unique=True, blank=True)
    title = models.CharField(max_length=300)
    blurb = models.TextField(blank=True, default='')
    pages = models.IntegerField(blank=True, null=True)
    authors = models.ManyToManyField(Author, blank=True)
    awards = models.ManyToManyField(Award, blank=True)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return f'{self.title}'
    def display_tag(self): # not recommended as it's an expensive query
        return ', '.join(i.tag for i in self.tags_for_this_book.all())
        """
        The above is equivalent to
        tags = []
        for i in self.tags_for_this_book.all():
            tags.append(i.tag)
        return ", ".join(tags)
        """
        

class Review(models.Model):
    RATING_CHOICES = (
        ('4' , 'Outstanding'),
        ('3' , 'Good'),
        ('2' , 'Not good'),
        ('1' , 'Bad')
    )
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, blank=True)
    review = models.TextField(blank=True)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE, related_name='reviews_for_this_book')


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)
    books = models.ManyToManyField('book.Book', related_name='tags_for_this_book')
    def save(self, force_insert=False, force_update=False):
        self.tag = self.tag.lower()
        super(Tag, self).save(force_insert, force_update) #super().save(force_insert, force_udpate) should work in new versions


