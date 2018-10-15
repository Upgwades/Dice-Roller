import argparse
import operator as op
import random
import re
import sys

british_insults = ['Tosser',
 'Wanker',
 'Slag',
 'No better than those Cheese Eating Surrender Monkeys',
 'Someone has Lost the plot.',
 'Daft Cow',
 'Arsehole',
 'Barmy',
 'Chav',
 'Dodgy',
 'Manky',
 'Minger',
 'Muppet',
 'Naff',
 'Nutter',
 'Pikey',
 'Pillock',
 'Plonker',
 'Prat',
 'Scrubber',
 'Trollop',
 'Uphill Gardener',
 'Twit',
 'Knob Head',
 'Piss Off',
 'Bell End',
 'Lazy Sod',
 'Skiver',
 'Knob Gobbler',
 'Wazzock',
 'Ninny',
 'Berk',
 'Airy-fairy',
 'Ankle-biter',
 'Arse-licker',
 'Arsemonger',
 'Chuffer',
 'You are Daft as a bush',
 "This one's Dead from the neck up",
 'Clearly your brain has gone to the dogs',
 'Ligger',
 'You are Like a dog with two dicks',
 'Mad as a bag of ferrets',
 'Maggot',
 'What a Mingebag',
 "This one's not Not batting on a full wicket",
 'You are Plug-Ugly',
 ]

def roll_dice(dice):
   """
   Take in a string that resembles a dice expression and produce an output
   ex. dice = '3d10'
   """
   try:
        total = []

        # Sometimes lazy assholes don't put a number infront of the dice
        if dice[0] == 'd' or dice[0] == 'D': dice = '1' + dice
        dice = re.split('[dD]',dice)

        # Why would someone roll 0 of something??
        if int(dice[0]) == 0: return 0
        if int(dice[1]) == 0: return 0

        for _ in range(int(dice[0])):
          total.append(str(random.randint(1,int(dice[1]))))
        combined = '(' + ' + '.join(total) + ')'
        return combined
   except Exception as e:
       print('Dice roller problem, PANIC, \n {}'.format(e))


def convert_int(number):
    """
    Convert and evaluate ints else return None
    """
    try:
        assert(isinstance(int(number),int))
        return number
    except Exception as e:
        return None

def convert_ops(operator):
    """
    Convert and evaluate a math operator else return None
    """
    ops = ['+','-','*','/']
    try:
        assert(operator in ops)
        return operator
    except Exception as e:
        return None

def convert_dice(dice):
    """
    Convert and evaluate a dice expression else return None
    """
    dice_pattern = '^(\d+)?([dD])(\d+)$'
    try:
        match = re.match(dice_pattern, dice)
        assert(match)
        return str(roll_dice(match.group(0)))
    except Exception as e:
        return None

def transmogrifier(input):
    """
    Simple generator to try and match values in the list to something that
    can be used. Checks if something is an int, math operator, or a
    valid dice expression and yields it back to the caller
    Will raise an error if a value doesn't match anything
    """
    for value in input:
        integer = convert_int(value)
        operator = convert_ops(value)
        dice = convert_dice(value)

        if integer: yield integer
        elif operator: yield operator
        elif dice: yield dice
        else: raise ValueError(random.choice(british_insults))

if __name__ == '__main__':
    """
    A lovingly crafter tool to take in dice roll and spit out nice clean
    wholegrain values
    Input:
    input(str): pos-arg with int and dice values mixed in,
    ex. '!r 5 - 1 + 1 + 1d7 - 2d10 + 2d10 + d10'
    """
    try:
        # Accept 1 positional arg as input
        parser = argparse.ArgumentParser()
        parser.add_argument("input")
        args = parser.parse_args()

        print('This is what I was given {}'.format(args.input))
        ops = ['+','-','*','/']
        input = args.input

        assert(input.startswith('!r'))

        # Remove the waste of space '!r'
        input = input.replace('!r','')
        input = input.replace(' ','')

        # Make spacing consistent
        for op in ops:
            input = input.replace(op, ' {} '.format(op))

        # Final split on clean string
        input = input.split(' ')

        # Run the list through a generator function to convert elements
        input = ' '.join([str(item) for item in transmogrifier(input)])

        # Eval is generally avoided like the plague but, the input goes through
        # enough check to convince the dev that it's ok here
        print('This is what I evaluated {}'.format(input))
        print('Oi! the result is {}'.format(eval(input)))

    except Exception as e:
        print(e)
    finally:
        sys.exit()
