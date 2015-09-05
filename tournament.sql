-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create database "tournament" and connect to that database before creating tables
--
-- Code to Drop and recreate table at import, used from:
--      url: https://discussions.udacity.com/t/helpful-hints-for-project-2/17994
\c vagrant
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Create a player table that has: id serial (primary key), name text

create table player ( id SERIAL PRIMARY KEY, name TEXT );


-- Create a match table that has: match_id (primary key), winner, loser, draw
--
-- First Version: match::    id serial primary key,
--                          winner integer REFERENCES player(id),
--                          loser integer REFERENCES player(id),
--                           draw boolean

create table match ( id SERIAL PRIMARY KEY,
                     winner INTEGER REFERENCES player(id),
                     loser INTEGER REFERENCES  player(id),
                     draw BOOLEAN);


-- Create View win_total :: table with cols-->  player.id as winner_id,
--                                              player.name as winner_name,
--                                              count(match.winner) as wins

create view win_total as select player.id as winner_id, player.name as winner_name,
                                count(match.winner) as wins
                                from player
                                    left join match
                                        on (player.id = match.winner and match.draw = False)
                                        group by player.id;


-- Create View loss_total :: table with cols--> player.id as loser_id,
--                                              player.name as loser_name,
--                                              count(match.loser) as losses

create view loss_total as select player.id as loser_id, player.name as loser_name,
                                    count(match.loser) as losses
                                    from player
                                        left join match
                                            on (player.id = match.loser and match.draw=False)
                                            group by player.id;


-- Create View draw_total :: table with cols--> drawer_id,
--                                              drawer_name,
--                                              draws

create view draw_total as select player.id as drawer_id, player.name as drawer_name,
                            count(match.draw) as draws
                            from player
                                left join match
                                    on ((player.id = match.loser and match.draw = True) or
                                    ( player.id=match.winner and match.draw = True))
                                    group by player.id;


-- Create View match_total :: table with cols-->    total,
--                                                  id

create view match_total as select count(match.winner) as total, player.id as id
                                from player
                                    left join match
                                        on player.id=match.winner or player.id=match.loser
                                        group by player.id;


-- Create View standings :: table with cols-->  id,
--                                              name,
--                                              wins,
--                                              draws,
--                                              losses,
--                                              matches
--
-- A Complex table that "left joins" player to: win_total (for wins),
--                                              draw_total (for draws), loss_total (for losses),
--                                              match_total (for matches)

-- Ordered by Values  Wins :: 3 points
--                    Draws :: 1 points
--                    Losses :: -1 points
--                  (in tournament.py)

create view standings as select player.id as id, player.name as name, win_total.wins as wins,
                                draw_total.draws as draws,
                                loss_total.losses as losses, match_total.total as matches
                                from player
                                    left join win_total
                                        on player.id = win_total.winner_id
                                    left join draw_total
                                        on player.id = draw_total.drawer_id
                                    left join loss_total
                                        on player.id = loss_total.loser_id
                                    left join match_total
                                        on player.id = match_total.id;
