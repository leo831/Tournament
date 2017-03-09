-- Table definitions for the tournament project.

--
-- Put your SQL 'create table' statements in this file; also 'create view'

-- statements if you choose to use it
.
--
-- You can write comments in this file by starting them with two dashes, like

-- these lines here.




--Crate database
CREATE DATABASE tournament;

\c tournament;

--crate player table
CREATE TABLE player(
    id serial primary key,
    name TEXT
    );

--Create match table
CREATE TABLE matches(
    match_id SERIAL primary key,
    winner integer references player(id),
    loser integer references player(id)

    );

CREATE VIEW  standings AS
 SELECT player.id, player.name, (SELECT count(*) FROM matches WHERE matches.winner = player.id) AS wins,(SELECT COUNT(*) FROM matches where player.id IN(winner, loser)) AS matches FROM player;