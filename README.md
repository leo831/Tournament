# Tournament
 * Tournament for Udacity's Full Stack Web Developer Nanodegree.
 * Created a Schema to store the players data while at the same time create and run queries.
 * Author: Leobardo Lara

## Requirements
Download the latest version of vagrant and also the tournament files.
## Instructions 
 1. Open cmd or Terminal and go to vagrant folder.
 2. Run Vagrant by running <code>vagrant up</code> and then <code>vagrant ssh</code>
 3. Now navegate to the tournament folder <code>cd vagrant/tournament</code>
 4. To run the tournament test file run this line <code>python tournament_test.py</code>
 
## Result

<code>vagrant@vagrant-ubuntu-trusty-32:/vagrant/Tournament$ python tournament_test.py</code>
 
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired. 
Success! All tests pass!
