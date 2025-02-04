
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

pza = Pizza(['cheese', 'tomatoes'])
print (pza.margherita())
print (pza.prosciutto())
pza_1 = Pizza(['apple']*4)
print (pza_1)