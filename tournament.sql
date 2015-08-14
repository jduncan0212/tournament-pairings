-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create database "tournament" and connect to that database before creating tables
\c vagrant
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Create a player table that has: id serial (primary key), name text
create table player ( id SERIAL PRIMARY KEY, name TEXT );


-- Create a match table that has: match_id (primary key), tournment_id() REFERENCES tournament(id), winner, loser
--
-- First Version: match: id serial primary key, winner integer REFERENCES player(id), loser REFERENCES player(id)
create table match ( id SERIAL PRIMARY KEY,
                     winner INTEGER REFERENCES player(id),
                     loser INTEGER REFERENCES  player(id) );



-- Create View wintotal
create view win_total as select player.id, player.name,
                        count(match.winner) as wins from player left join match
                        on player.id = match.winner group by player.id;

create view match_total as select  count(match.winner) as total, player.id from
                        player left join match on player.id=match.winner or
                        player.id=match.loser group by player.id;

create view standings as select win_total.id, win_total.name, wins, total from
                        win_total left join match_total on win_total.id=match_total.id;

--Create a Tournaments table that has: tournament_id (primary key), rounds, winner



