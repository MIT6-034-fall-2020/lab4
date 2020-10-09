# MIT 6.034 Lab 4: Rule-Based Systems
# Written by 6.034 staff

from production import IF, AND, OR, NOT, THEN, DELETE, forward_chain, pretty_goal_tree
from data import *
import pprint

pp = pprint.PrettyPrinter(indent=1)
pprint = pp.pprint

#### Part 1: Multiple Choice #########################################

ANSWER_1 = '2' # can only assert consequent

ANSWER_2 = '4' # don't change the assert

ANSWER_3 = '2'

ANSWER_4 = '0'

ANSWER_5 = '3'

ANSWER_6 = '1'

ANSWER_7 = '0' # there's already a match in the data

#### Part 2: Transitive Rule #########################################

# Fill this in with your rule 
transitive_rule = IF( AND( '(?x) beats (?z)',
                           '(?z) beats (?y)' ), 
                    THEN( '(?x) beats (?y)' ) )

# You can test your rule by uncommenting these pretty print statements
#  and observing the results printed to your screen after executing lab1.py
# pprint(forward_chain([transitive_rule], abc_data))
# pprint(forward_chain([transitive_rule], poker_data))
# pprint(forward_chain([transitive_rule], minecraft_data))


#### Part 3: Family Relations #########################################

# Define your rules here. We've given you an example rule whose lead you can follow:
friend_rule = IF( AND("person (?x)", "person (?y)"), THEN("friend (?x) (?y)", "friend (?y) (?x)") )
identity_rule = IF( AND('person (?x)', 'person (?x)'),  THEN( 'same (?x) (?x)' ) )
sibling_rule = IF( AND( 'parent (?p) (?m)', 'parent (?p) (?n)', NOT( 'same (?m) (?n)' ) ), 
                THEN( 'sibling (?m) (?n)', 'sibling (?m) (?n)' ) )
child_rule = IF( AND('parent (?p) (?c)', NOT( 'same (?p) (?c)')), 
                THEN('child (?c) (?p)') )
cousin_rule = IF( AND( 'parent (?a) (?x)', 'parent (?b) (?y)',
                        'sibling (?a) (?b)', NOT('sibling (?x) (?y)')),
                THEN('cousin (?x) (?y)', 'cousin (?y) (?x)'))
grandrelation_rule = IF( AND('parent (?a) (?b)', 'parent (?b) (?c)'),
                THEN('grandparent (?a) (?c)', 'grandchild (?c) (?a)'))




# Add your rules to this list:
family_rules = [ identity_rule, sibling_rule, child_rule, cousin_rule, grandrelation_rule ]

# Uncomment this to test your data on the Simpsons family:
# pprint(forward_chain(family_rules, simpsons_data, verbose=False))

# These smaller datasets might be helpful for debugging:
# pprint(forward_chain(family_rules, sibling_test_data, verbose=True))
# pprint(forward_chain(family_rules, grandparent_test_data, verbose=True))

# The following should generate 14 cousin relationships, representing 7 pairs
# of people who are cousins:
harry_potter_family_cousins = [
    relation for relation in
    forward_chain(family_rules, harry_potter_family_data, verbose=False)
    if "cousin" in relation ]

# To see if you found them all, uncomment this line:
# pprint(harry_potter_family_cousins)
# print(len(harry_potter_family_cousins)) # Should be 14

#### Part 4: Backward Chaining #########################################

# Import additional methods for backchaining
from production import PASS, FAIL, match, populate, simplify, variables

def backchain_to_goal_tree(rules, hypothesis):
    """
    Takes a hypothesis (string) and a list of rules (list
    of IF objects), returning an AND/OR tree representing the
    backchain of possible statements we may need to test
    to determine if this hypothesis is reachable or not.

    This method should return an AND/OR tree, that is, an
    AND or OR object, whose constituents are the subgoals that
    need to be tested. The leaves of this tree should be strings
    (possibly with unbound variables), *not* AND or OR objects.
    Make sure to use simplify(...) to flatten trees where appropriate.
    """
    raise NotImplementedError


# Uncomment this to test out your backward chainer:
# pretty_goal_tree(backchain_to_goal_tree(zookeeper_rules, 'opus is a penguin'))


#### Survey #########################################

NAME = None
COLLABORATORS = None
HOW_MANY_HOURS_THIS_LAB_TOOK = None
WHAT_I_FOUND_INTERESTING = None
WHAT_I_FOUND_BORING = None
SUGGESTIONS = None


###########################################################
### Ignore everything below this line; for testing only ###
###########################################################

# The following lines are used in the tester. DO NOT CHANGE!
print("(Doing forward chaining. This may take a minute.)")
transitive_rule_poker = forward_chain([transitive_rule], poker_data)
transitive_rule_abc = forward_chain([transitive_rule], abc_data)
transitive_rule_minecraft = forward_chain([transitive_rule], minecraft_data)
family_rules_simpsons = forward_chain(family_rules, simpsons_data)
family_rules_harry_potter_family = forward_chain(family_rules, harry_potter_family_data)
family_rules_sibling = forward_chain(family_rules, sibling_test_data)
family_rules_grandparent = forward_chain(family_rules, grandparent_test_data)
family_rules_anonymous_family = forward_chain(family_rules, anonymous_family_test_data)
