from src.card import Card

class Life(Card):
    # Cards that are turned over when player looses a 'life'
    description = ""
    count = 3

    flavor_texts = [
        "todo",
        "todo",
        "todo",
    ]

    # A dict that holds all defined cards by:
    # string of class name -> type
    all_types = {}
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Register each subclass in the all_cards dictionary
        cls.all_types[cls.__name__] = cls

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def sorted_types(cls):
        return sorted(cls.all_types.values(), key=lambda c: c.name)


# Teams are defined below
class Cashless(Life):
    flavor_texts = [
        '''"Big money... No whammies..."\n~ Lucky Luke''',
        '''"Broke is just a state of wallet, not a state of mind."\n~ Sylvia the Scrounger''',
        '''"Lost my fortune, but never my freedom!"''',
    ]

class Faithful(Life):
    flavor_texts = [
        '''"Our bond is our strength; where one goes, the others follow."\n~Sister Serene''',
        '''"True belief isn't seen in the light—it's felt in the darkness among the lions."\n~ Cassandra the Convicted''',
        '''"Don't walk the tightrope. Dance it."''',
    ]

class Forgotten(Life):
    flavor_texts = [
        '''"The real master is never in the limelight. Always the shadows."\n~ M.C. Echo''',
        '''"Dusty books hold legends."\n~ Misty-eyed Mira''',
        '''"There's always a sharp end to the applause."''',
    ]

class Lost(Life):
    flavor_texts = [
        '''"'Losing your way' is the first step to... Something!"\n~Willy Wayward''',
        '''"Where there's darkness, there's stars."\n~M.M. Madeline''',
        '''"Life is a maze. Only one way out!"''',
    ]

class Proud(Life):
    flavor_texts = [
        '''"I'm dealing with fools and trolls and soft targets.\nI don't have time for these clowns."\n~ Charles the Smiler''',
        '''"Bow down or stand back—those are your options when royalty steps into the ring."\n~ Lady Vanessa the Vain''',
        '''"My legacy will tell of my greatness, your legacy will be that you once saw me perform."''',
    ]

class Vengeful(Life):
    flavor_texts = [
        '''"An eye for an eye, a tooth for a tooth,\nand for every slight, a relentless pursuit."\n~ Vera''',
        '''"Everyone looks at the ringmaster's flaming hoop.\nThey forget the whip."\n~The Scorpio''',
        '''"Never miss twice."''',
    ]
