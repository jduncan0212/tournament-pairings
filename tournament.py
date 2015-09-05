#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db_conn = connect()
    db_cursor = db_conn.cursor()
    db_cursor.execute('DELETE from match;')
    db_conn.commit()
    db_conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db_conn = connect()
    db_cursor = db_conn.cursor()
    db_cursor.execute('DELETE from player')
    db_conn.commit()
    db_conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db_conn = connect()
    db_cursor = db_conn.cursor()
    db_cursor.execute('SELECT count(player.id) from player')
    count = db_cursor.fetchone()
    db_conn.commit()
    db_conn.close()
    return int(count[0])


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db_conn = connect()
    db_cursor = db_conn.cursor()
    sql_insert = "insert into player (name) values (%s);"
    db_cursor.execute(sql_insert, (name,))
    db_conn.commit()
    db_conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    list_of_players = []
    db_conn = connect()
    db_cursor = db_conn.cursor()

    # use a points system of    win:: 3 points
    #                           draw:: 1 point
    #                           loss:: -1 point
    # to order query
    # same as in playStandings
    sql_player_standings = (
                "select id, name, wins, matches"
                " from standings"
                " order by (3*(wins)+(draws)-(losses)) desc;")
    db_cursor.execute(sql_player_standings)
    results = db_cursor.fetchall()
    for record in results:
        list_of_players.append((record[0], record[1], record[2], record[3]))
    db_conn.commit()
    db_conn.close()
    return list_of_players


def reportMatch(winner, loser, draw=False):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db_conn = connect()
    db_cursor = db_conn.cursor()
    sql_match_report = ('insert into match (winner, loser, draw)'
                        'values (%s, %s, %s)')
    db_cursor.execute(sql_match_report, (winner, loser, draw))
    db_conn.commit()
    db_conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db_conn = connect()
    db_cursor = db_conn.cursor()

    # use a points system of    win:: 3 points
    #                           draw:: 1 point
    #                           loss:: -1 point
    # to order query
    sql_pairings = (
                "select id, name"
                "   from standings"
                "       order by (3*(wins)+(draws)-(losses)) desc;")
    db_cursor.execute(sql_pairings)

    # A list of entries is returned to us
    # with each entry as a two-item tuple
    all_players = db_cursor.fetchall()

    # I used list comprehensions to:
    #       1.) separate the result pairs into --> a list of singlets.
    #       2.) then to add them in to--> a list of tuples, each with 4 entries.
    #
    # The reason I did not use the "Zip" function is becauese I found it more
    # diffcult to understand than list comphresions and didn't like the
    # idea of having to rely on something I couldn't quite wrap my head around
    # :(
    #
    atomic_list = [single for tup in all_players for single in tup]
    tuple_quad = [(atomic_list[i], atomic_list[i+1], atomic_list[i+2],
                   atomic_list[i+3]) for i in range(0, len(atomic_list)-3, 4)]
    db_conn.commit()
    db_conn.close()
    return tuple_quad
