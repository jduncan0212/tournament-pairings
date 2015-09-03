#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *

def testDeleteMatches():
    deleteMatches()
    print "1. Old matches can be deleted."


def testDelete():
    deleteMatches()
    deletePlayers()
    print "2. Player records can be deleted."


def testCount():
    deleteMatches()
    deletePlayers()
    c = countPlayers()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "3. After deleting, countPlayers() returns zero."


def testRegister():
    deleteMatches()
    deletePlayers()
    registerPlayer("Chandra Nalaar")
    c = countPlayers()
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "4. After registering a player, countPlayers() returns 1."


def testRegisterCountDelete():
    deleteMatches()
    deletePlayers()
    registerPlayer("Markov Chaney")
    registerPlayer("Joe Malik")
    registerPlayer("Mao Tsu-hsi")
    registerPlayer("Atlanta Hope")
    c = countPlayers()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    deletePlayers()
    c = countPlayers()
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "5. Players can be registered and deleted."


def testStandingsBeforeMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("Melpomene Murray")
    registerPlayer("Randy Schwartz")
    standings = playerStandings()
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before "
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each playerStandings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        print matches1, matches2, wins1, wins2
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "
                         "even if they have no matches played.")
    print "6. Newly registered players appear in the standings with no matches."


def testReportMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("Bruno Walton")
    registerPlayer("Boots O'Neal")
    registerPlayer("Cathy Burton")
    registerPlayer("Diane Grant")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    standings = playerStandings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "7. After a match, players have updated standings."



def testPairings():
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")      # gets to win rd 1
    registerPlayer("Fluttershy")            # loses in rd 1
    registerPlayer("Applejack")             # draws in rd 1
    registerPlayer("Pinkie Pie")            # draws in rd 1

    ## Added two extra players so we can get two players with one win at the end
    ## Of round one, incorporating draws

    registerPlayer("Hula Hoop")             # gets to win in rd 1, also
    registerPlayer("Fluffy Marshmellow")    # loses in rd 1, :(

    standings = playerStandings()
    [id1, id2, id3, id4, id5, id6] = [row[0] for row in standings]
    [name1, name2, name3, name4, name5, name6] = [row[1] for row in standings]
    playerdict = {name1:id1, name2:id2, name3:id3, name4:id4, name5:id5, name6:id6}

    reportMatch(playerdict["Twilight Sparkle"], playerdict["Fluttershy"])
    # report a draw
    reportMatch(playerdict["Applejack"], playerdict["Pinkie Pie"], True)
    reportMatch(playerdict["Hula Hoop"], playerdict["Fluffy Marshmellow"])
    pairings = swissPairings()
    if len(pairings) != 3:
        print pairings
        raise ValueError(
            "For six players, swissPairings should return three pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4), (pid5, pname5, pid6, pname6)] = pairings
    correct_pairs = set([frozenset([playerdict["Twilight Sparkle"], playerdict["Hula Hoop"]]),
                            frozenset([playerdict["Applejack"], playerdict["Pinkie Pie"]]),
                            frozenset([playerdict["Fluttershy"], playerdict["Fluffy Marshmellow"]])])

    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4]), frozenset([pid5, pid6])])


    reportMatch(pairings[0][0], pairings[0][2])
    reportMatch(pairings[1][0], pairings[1][2])
    reportMatch(pairings[2][0], pairings[2][2])

    # only comparing players with one win, for now --9/2
    if correct_pairs != actual_pairs:
        print [(p[1],p[3]) for p in pairings]
        raise ValueError(
            "After one match, players with one win should be paired.")

    print [(p[1],p[3]) for p in pairings]
    print "8. After one match, players with one win are paired."


if __name__ == '__main__':
    testDeleteMatches()
    testDelete()
    testCount()
    testRegister()
    testRegisterCountDelete()
    testStandingsBeforeMatches()
    testReportMatches()
    testPairings()
    print "Success!  All tests pass!"


