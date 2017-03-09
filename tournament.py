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
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("DELETE from matches")
    dbConn.commit()
    dbConn.close()


def deletePlayers():
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("DELETE from player")
    dbConn.commit()
    dbConn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("SELECT count(name) from player")
    players = c.fetchone()[0]
    dbConn.close()
    return players

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("INSERT INTO player (name) VALUES(%s)", (name,))
    dbConn.commit()
    dbConn.close()


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
    
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("SELECT * from standings")
    standings = c.fetchall()
    dbConn.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES(%s , %s)", (winner, loser,))
    dbConn.commit()
    dbConn.close()
 
 
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
    dbConn = connect()
    c = dbConn.cursor()
    c.execute("SELECT * FROM standings ORDER BY wins DESC")
    standings = c.fetchall()
    dbConn.close()

    i=0
    pairings = list()
    while i < len(standings):
        playerId = standings[i][0]
        playerName = standings[i][1]
        player2id = standings[i+1][0]
        player2name = standings[i+1][1]
        pairings.append((playerId,playerName,player2id,player2name))
        i=i+2

    return pairings


