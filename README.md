# Swiss Tournament Pairings
<h4> Tournament-Pairings: Udacity FSWD Project 2 </h4>

This repository is designed provide a backend to support a hypothetical tournament—such as may be hosted on a website or forum of some kind. Just to be deliberately boring, the most obvious example is a chess tournament—if that is just too much think of a chocolate eating tournament. :chocolate_bar:

Included are: 

|Filename | Purpose|
|-------|-----|
| tournament.sql| Create the necessary database, tables, views for the tournament data |
| tournament.py | Manipulate the database to add or remove tournament results (e.g. Jack loses to Jill ) |
| tournament_test.py | A file containing unit tests for tournament.py & tournament.sql |
| gistfile1.py | A file which simulates matches to test tournament.py & tournament.sql |
| .gitignore      | gitignore file, to ignore .pyc & .vagrant files |


<b>This project depends on both:</b>

* Python 2.7
  * The psycopg2 module
    * See: http://initd.org/psycopg/docs/install.html#install-from-package
* A Postgresql Database 

<b> Given these dependecies the *easiest* way to get the project up and working would be for you to download & install the: </b><br>

1. Vagrant virtual machine wrapper
2. VirtualBox
<br>following that...
3. Clone Udacity's starting repository for this project.

4. <b>And,</b> then clone *this repository* into the 'vagrant' directory. 

<br>
<h4> Details for each of this steps follows below ** : </h4> 
--Alternatively, see this link for a different guide: [Udacity.com Vagrant Install Guide](https://www.udacity.com/wiki/ud197/install-vagrant)


<h5>1.) Downloading and Installing Vagrant</h5>
  1. Download the version of vagrant installer appropriate to your operating system ( MAC/Windows/Linux ) and processor type (32 vs 64 bits ):
    * here: [vagrantup](https://www.vagrantup.com/downloads)
  2. Install from the downloaded installer
  3. Allow any network or firewall permissions as prompted.
  4. vagrant will automatically be added to your system path; qtd. from vagrantup.com:

  >The installer will automatically add vagrant to your system path so that it is available in terminals. If it is not found, please try logging out and logging back into your system (this is particularly necessary sometimes for Windows).

#####2.) Downloading and Installing the VirtualBox [Hypervisor](https://en.wikipedia.org/wiki/Hypervisor)
  1. Down the VirtualBox "Platform Package" appropriate to your operating system:
    * here: [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
  2. Install from the downloaded installer, ( e.g. on Mac OS X 10 doubleclick on the download icon and then doubleclick on the install package icon to run the installer )

#####3.) Clone the VM configuration files and vanilla project files:
  1. Navigate to the [Udacity fullstack repository](http://github.com/udacity/fullstack-nanodegree-vm) here on github:
    * Clone their repository using the Clone Icon (lower right sidebar):

    <b>Or</b>
    * CD to you home directory, then Clone from terminal with Git with these commands:

      ```cd ~```

      ```git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack```

#####4.) [Option 1] Clone this repository in the 'vagrant' directory of the fullstack directory( from step 3 ):
  1. Navigate 'vagrant' subdirectory inside your 'fullstack' directory:
    * Clone this project using the Clone Icon (lower right sidebar)

    <b>Or</b>
    * Clone from terminal with Git with the commands:

      ```git clone http://github.com/jduncan0212/tournament-pairings```

#### Alternatively,...

#####4.) [Option 2] Fetch and Merge this repository with the 'tournament' sub-sub-directory of the 'fullstack' directory ( from step 3 ):
  1. Navigate 'tournament' subdirectory inside your 'fullstack' directory.
    * Such as by the command (assuming you are in the 'fullstack' directory) : `cd vagrant/tournament/`
  2. Fetch this project with the command (make sure you are on the master branch, you should be by default):


      ```git fetch http://github.com/jduncan0212/tournament-pairings```
  3. Merge with the vanilla tournament directory with the command:


      ```git merge FETCH_HEAD --strategy-option theirs```
      
      1. This option should Resolve all Merge Conflicts in favor of this version——no worries; the earlier version is just the code outline.
      2. Enjoy
      3. :satisfied:


<hr>
###Running Vagrant:

  **Wait?!** You went through all that trouble to install Vagrant, surely you now want to run it? To do so, navigate to the 'tournament' subdirectory inside the 'fullstack' directory and from the terminal enter:
  
  ```vagrant up```
  
  and 
  
  ```vagrant ssh```
  
  to see the project files:
  
  ```cd /vagrant```
  
  :congratulations:


<hr>
###Testing that it works as intended:

*But does it actually work?* 

You can use the simple command:
```cd tournament/```

* full path:
 *  `cd /vagrant/tournament/`

and test using the built in unit test module ( tournament_test.py ):
```python tournament_test.py tournament.py```
* You should see a message with cutsie names and then "Success!  All tests pass!"
* Of course, you can create your own tests and/or modify tournament_test.py if you find these tests lacking.


<hr>
#### Git install, if not already present: 

** Since you are using github I assume you have Git installed——if not——it is in fact required also ( sorry for another thing! )<br>
** You can download Git [here] (http://git-scm.com/downloads)
