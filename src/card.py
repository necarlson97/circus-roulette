from src.utils import NamedClass

import logging
logger = logging.getLogger("HotMech")

class Card(NamedClass):
    """
    Abstract class, that each specific type of card will sub-class
    Then each instance of a subclass is the individual card,
    """

    # Steps defined by the subclass type.
    # A list of 'Step' types, that get initialized
    # to create this individual card's steps
    description = "todo desc"
    flavor_text = "todo flavor"

    # How many times does it appear in the deck?
    # TODO slightly different images?
    count = 1

    # A dict that holds all defined cards by:
    # string of class name -> type
    all_types = {}
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Register each subclass in the all_cards dictionary
        # TODO SLOPPY
        if cls.__name__ != "Life":
            cls.all_types[cls.__name__] = cls

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def sorted_types(cls):
        return sorted(cls.all_types.values(), key=lambda c: c.name)

    @classmethod
    def reprints(cls):
        return {
            # Premonition: 2,
            # HandOff: 0,
            # Silence: 0,
        }

"""
Below, all card types are defined:
"""
class PullHarder(Card):
    count = 2
    description = "Gun holder shoots themself (again)"
    flavor_text = (
        '"Second verse, same as the first.\n'
        'A little bit louder and a whole lot worse."'
        '\n~ Pogo, the Clown'
    )

    def human_name():
        return "Pull Harder!"

class SleightOfHand(Card):
    count = 2
    description = (
        "Target player chooses a loaded round to swap with one "
        "from their pocket"
    )
    flavor_text = (
        '"Now you see it, now you... still see it.\n'
        'But trust me, it’s not where you think it is."'
        '\n~ The Great Vanisho'
    )

class HandOff(Card):
    count = 2
    description = (
        "Force any player to take the gun"
    )
    flavor_text = (
        '"Take it, take it! I insist. After all, sharing is caring...\n'
        'especially the risk."'
        '\n~ Lenny the Lion Tamer'
    )

class Premonition(Card):
    count = 6
    description = (
        "Inspect the gun. Take it, look it over - but do not open it. Then give it back to the gun holder"
    )
    flavor_text = (
        '"Forewarned is forearmed. Especially useful when the arms in '
        'question are potentially deadly."'
        '\n~ Dr. Orville'
    )

class PatDown(Card):
    count = 2
    description = (
        "Inspect a players pocket rounds "
        "(just look, no pulling apart rounds)"
    )
    flavor_text = (
        '"Trust is good, but checking is better.\n'
        'Especially when the stakes are this high."'
        '\n~ Fish Fingers'
    )

class PickPocket(Card):
    count = 1
    description = (
        "Choose a round from another pocket, swap it with one of your own"
    )
    flavor_text = (
        '"What\'s yours is mine, and what\'s mine is... also mine.\n'
        'That\'s the magic of misdirection."'
        '\n~ Sly Simon'
    )

class Betrayal(Card):
    count = 2
    description = (
        "The gun holder fires at anyone (victim can win the casing)"
    )
    flavor_text = (
        '"A pie in the face, but a knife in the back."'
        '\n~ Reverend Jester Jones'
    )

class Spin(Card):
    count = 2
    description = (
        "Spin the cylinder"
    )
    flavor_text = (
        '"Time to turn your luck around!"'
        '\n~ Twirly Tina'
    )

    def human_name():
        return "Spin!"

class CeilingShot(Card):
    count = 2
    description = (
        "Fire the gun into the air\n(nobody gets the casing)"
    )
    flavor_text = (
        '"One for the big man upstairs!"'
        '\n— Cannonman Carl'
    )

class VodkaShot(Card):
    count = 1
    description = (
        "The next shot provides an extra casing"
    )
    flavor_text = (
        'Little liquid courage to double your chances—or your regrets."'
        '\n~ the Vagrant Virtuoso'
    )

class OneForOne(Card):
    count = 1
    description = (
        "Gun holder shoots at you. Then you choose a target for "
        "the gun holder to shoot at."
    )
    flavor_text = (
        '"What goes around comes around, often faster than you expect."'
        '\n~ Petra the Quickdraw'
    )

class Wrestle(Card):
    count = 1
    description = (
        "Gun holder shoots at you. Then you get the gun."
    )
    flavor_text = (
        '"Possession may be only half the story,\n'
        'but it\'s 9/10ths of the law!"'
        '\n— Grapple Gary, the Ground-and-Pound Clown'
    )

class Flirt(Card):
    count = 1
    description = (
        "Choose a player to discard a card"
    )
    flavor_text = (
        '"A wink, a smile, and oh, what\'s this?\n'
        'You seem to have dropped something."'
        '\n~ Felicity the Fanciful'
    )

class Clairvoyance(Card):
    count = 4
    description = (
        "Inspect another player's cards"
    )
    flavor_text = (
        '"The future is in your hands."'
        '\n— The All-Seeing Salvatore'
    )

class PublicShaming(Card):
    count = 2
    description = (
        "Target player reveals their hand to all others"
    )
    flavor_text = (
        '"A little exposure keeps everyone honest, '
        'embarrassed, and entertained!"'
        '\n~ Madame Blush'
    )

class Silence(Card):
    count = 2
    description = (
        "Cancel a card"
    )
    flavor_text = (
        '"..."'
        '\n— Marx, the Mime'
    )

class BiteBullet(Card):
    count = 2
    description = (
        "Gun holder shoots themselves, but is awarded 2 casings "
        "if they lose a life"
    )
    flavor_text = (
        '"You\'ve got to eat lead to get ahead. '
        'Just make sure the bite\'s worth the chew."'
        '\n~ "Chomper" Malone'
    )


# Card ideas:
"""
* Place gun on the table and spin (like spin the bottle). Whoever it points at
has to shoot themselves, then becomes gun holder.
"""

# Unused flavor text:
"""
"Misery loves company, especially if it's your own."
~ Slick Sammy the Ringmaster

"I'm dealing with fools and trolls and soft targets. I don't have time for these clowns."
~ Charles the Smiler

"A little peek behind the curtain can save your neck. Or, at least delay the inevitable."
~ Cassandra the Seer

"One for courage, and one for luck. Cheers to shooting twice as much!"
~ Boris the Bold, the Bearded Lady
"""
