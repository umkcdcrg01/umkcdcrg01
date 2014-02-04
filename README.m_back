umkcdcrg01
==========
information from http://git-scm.com/doc



Charpter 1 git installation and config

Git's Three states

    Committed means that the data is safely stored in your local database. 
    Modified means that you have changed the file but have not committed it to your database yet. 
    Staged means that you have marked a modified file in its current version to go into your next commit snapshot.


    Git directory ---> working directory
    Working directory ---> staging area --->  and git directory.

    The basic Git workflow goes something like this:

        You modify files in your working directory.
        You stage the files, adding snapshots of them to your staging area.
        You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.

    Git comes with a tool called git config that lets you get and set configuration variables that control all aspects of how Git looks and operates. These variables can be stored in three different places:
        /etc/gitconfig file: Contains values for every user on the system and all their repositories. If you pass the option--system to git config, it reads and writes from this file specifically.
        
        ~/.gitconfig file: Specific to your user. You can make Git read and write to this file specifically by passing the --global option.
        
        config file in the git directory (that is, .git/config) of whatever repository you’re currently using: Specific to that single repository. Each level overrides values in the previous level, so values in .git/config trump those in /etc/gitconfig.

User Identity
    $ git config --global user.name "jackcrazy"
    $ git config --global user.email s.zhao.j@gmail.com

    notes:
        Again, you need to do this only once if you pass the --global option, because then Git will always use that information for anything you do on that system. If you want to override this with a different name or e-mail address for specific projects, you can run the command without the --global option when you’re in that project.

Your Diff Tool
    Another useful option you may want to configure is the default diff tool to use to resolve merge conflicts. Say you want to use vimdiff:

    $ git config --global merge.tool vimdiff

Checking Your Settings
    git config --list
    git config user.name

Git help
    git help <verb>
    git <verb> --help
    man git-<verb>
    ex: 
        git help config



Chapter 2 Git Basics

Getting a git repository
    
    Initializing a Repository in an Existing Directory
    $ git init
    notes:
        This creates a new subdirectory named .git that contains all of your necessary repository files — a Git repository skeleton. At this point, nothing in your project is tracked yet. (See Chapter 9 for more information about exactly what files are contained in the .git directory you just created.)
    $ git commit -m 'initial project version'
    $ git clone git://github.com/schacon/grit.git
    notes:
        That creates a directory named grit, initializes a .git directory inside it, pulls down all the data for that repository, and checks out a working copy of the latest version. If you go into the new grit directory, you’ll see the project files in there, ready to be worked on or used. If you want to clone the repository into a directory named something other than grit, you can specify that as the next command-line option:
        $ git clone git://github.com/schacon/grit.git mygrit

Recording Changes to the Repository

    Files life cycle in git:
    untracked --> unmodified --> modified --> staged ----(clone) ---> unmodified --(remove) --> untracked
    
    Remember that each file in your working directory can be in one of two states: tracked or untracked. Tracked files are files that were in the last snapshot; they can be unmodified, modified, or staged. Untracked files are everything else — any files in your working directory that were not in your last snapshot and are not in your staging area. When you first clone a repository, all of your files will be tracked and unmodified because you just checked them out and haven’t edited anything.

    As you edit files, Git sees them as modified, because you’ve changed them since your last commit. You stage these modified files and then commit all your staged changes, and the cycle repeats. 

Checking the Status of Your Files
    
    $ git status
    Let’s say you add a new file to your project, a simple README file. If the file didn’t exist before, and you run git status, you see your untracked file like so:

        $ vim README
        $ git status
            # On branch master
            # Untracked files:
            #   (use "git add <file>..." to include in what will be committed)
            #
            #   README
            nothing added to commit but untracked files present (use "git add" to track)
            NOTES:
                You can see that your new README file is untracked, because it’s under the “Untracked files” heading in your status output. Untracked basically means that Git sees a file you didn’t have in the previous snapshot (commit); Git won’t start including it in your commit snapshots until you explicitly tell it to do so. It does this so you don’t accidentally begin including generated binary files or other files that you did not mean to include. You do want to start including README, so let’s start tracking the file.

Tracking new files

    $ git add README

        Jack:gittest tonyalbums$ vi README
        Jack:gittest tonyalbums$ git status
        # On branch master
        # Untracked files:
        #   (use "git add <file>..." to include in what will be committed)
        #
        #   README
        nothing added to commit but untracked files present (use "git add" to track)
        ex:
            Jack:gittest tonyalbums$ git add README 
            Jack:gittest tonyalbums$ git status
            # On branch master
            # Changes to be committed:
            #   (use "git reset HEAD <file>..." to unstage)
            #
            #   new file:   README
            
Staging Modified Files

    if you changed a tracked file (ex: benchmarks.rb), and run "git status", you will get sth like this:
    $ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #   new file:   README
    #
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #
    #   modified:   benchmarks.rb   

    NOTES:
        'chnages not staged for commit' means that "benchmarks.rb" file that is tracked has been modified in the working directory but not yet staged. you need to run "git add benchmarks.rb" to stage it.

        git add command (it’s a multipurpose command — you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved)
        EX:
            $ git add benchmarks.rb
            $ git status
            # On branch master
            # Changes to be committed:
            #   (use "git reset HEAD <file>..." to unstage)
            #
            #   new file:   README
            #   modified:   benchmarks.rb
        NOTES:
            Everytime you change a file, before you commit, you need to stage it.

Ignoring Files          

    create a file  named .gitignore. 
    $ vi .gitignore
        # a comment - this is ignored
        # no .a files
        *.a
        # but do track lib.a, even though you're ignoring .a files above
        !lib.a
        # only ignore the root TODO file, not subdir/TODO
        /TODO
        # ignore all files in the build/ directory
        build/
        # ignore doc/notes.txt, but not doc/server/arch.txt
        doc/*.txt
        # ignore all .txt files in the doc/ directory
        doc/**/*.tx

Viewing Your Staged and Unstaged Changes
    
    Two questions you wanna know:
        What have you changed but not yet staged? 
        What have you staged that you are about to commit? 
    $ git status will give you a vague idea
    $ git diff shows you the exact lines added and moved

    $ git diff 
    this command Will compare what is in your working directory with what is in your staging area. The  result tells you the changes you’ve made that you haven’t yet staged.
    
    $ git diff --cached OR --staged
    This command tells:  what you’ve staged that will go into your next commit

    VERY IMPORTANT NOTES:
    It’s important to note that git diff by itself doesn’t show all changes made since your last commit — only changes that are still unstaged. This can be confusing, because if you’ve staged all of your changes, git diff will give you no output.
    simply speaking:
        if you staged some modified files, git diff wont tell you anything, else you use git diff --staged to see all the changes which has not been committed yet.

Committing your changes

    Now that your staging area is set up the way you want it, you can commit your changes. Remember that anything that is still unstaged — any files you have created or modified that you haven’t run git add on since you edited them — won’t go into this commit. They will stay as modified files on your disk.

    So everytime before you commit your file, do "git status" or "git diff" to check if everything is staged.

    $ git commit -m "Your message"


Skipping the Staging Area
    
    $ git commit -a -m "Your message"
    NOTE:
        -a means git will automatcially stage all the files and commit for you. You dont need to do "git add filename" by yourself

Removing files

    $ git rm filename
    The next time you commit, the file will be gone and no longer tracked. If you modified the file and added it to the index already, you must force the removal with the -f option. This is a safety feature to prevent accidental removal of data that hasn’t yet been recorded in a snapshot and that can’t be recovered from Git.

    $ git rm --cached filename
    you may want to do is to keep the file in your working tree but remove it from your staging area. In other words, you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your .gitignore file and accidentally staged it, like a large log file or a bunch of .a compiled files. To do this, use the --cached option:

Moving files (or Rename files)

    use $ git mv oldfile newfile
    Equals to
        $ mv oldfile newfile
        $ git rm oldfile
        $ git add newfile

Viewing the command history

    $ git log 
    OR a GUI
    $ gitk


Undoing things

changing your last commit
    
    $ git commit --amend
    As an example, if you commit and then realize you forgot to stage the changes in a file you wanted to add to this commit, you can do something like this:
        $ git commit -m 'initial commit'
        $ git add forgotten_file
        $ git commit --amend
        After these three commands, you end up with a single commit — the second commit replaces the results of the first.

Unstaging a staged file
    $ git reset HEAD A_Staged_file_name
    $ git status

Unmodifying a Modified File
    $ git checkout -- "ModifiedFIleNmae" 
    Don’t ever use this command unless you absolutely know that you don’t want the file.

Showing Your Remotes

    $git remote
    To see which remote servers you have configured, you can run the git remote command. It lists the shortnames of each remote handle you’ve specified. If you’ve cloned your repository, you should at least see origin — that is the default name Git gives to the server you cloned from:

    Jack:treebook tonyalbums$ git remote -v
        origin  https://github.com/jackcrazy/treebook.git (fetch)
        origin  https://github.com/jackcrazy/treebook.git (push)

        $ git remote add dccontrol https://github.com/matao/DControl.git
        $ git remote -v
            dccontrol   https://github.com/matao/DControl.git (fetch)
            dccontrol   https://github.com/matao/DControl.git (push)
            origin  https://github.com/matao/DControl.git (fetch)
            origin  https://github.com/matao/DControl.git (push)

Fetching and Pulling from Your Remotes

        $ git fetch dccontrol
            From https://github.com/matao/DControl
             * [new branch]      addSwitchDB -> dccontrol/addSwitchDB
             * [new branch]      linechart  -> dccontrol/linechart
             * [new branch]      master     -> dccontrol/master
        NOTES:
            After you do this, you should have references to all the branches from that remote, which you can merge in or inspect at any time.
            It’s important to note that the fetch command pulls the data to your local repository — it doesn’t automatically merge it with any of your work or modify what you’re currently working on. You have to merge it manually into your work when you’re ready.

        $ git pull
            If you have a branch set up to track a remote branch (see the next section and Chapter 3 for more information), you can use the git pull command to automatically fetch and then merge a remote branch into your current branch.
            git clone command automatically sets up your local master branch to track the remote master branch on the server you cloned from(assuming the remote has a master branch)
            git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you’re currently working on.

Pushing to Your Remotes
    
    Create a new repository on the command line
        git init
        git add README.md
        git commit -m "first commit"
        git remote add origin https://github.com/jackcrazy/gittest.git
        git push -u origin master
        
    Push an existing repository from the command line
        git remote add origin https://github.com/jackcrazy/gittest.git
        git push -u origin master

Inspecting a Remote branch

    $ git remote show origin OR dccontrol
    Notes:
        Jack:DControl tonyalbums$ git remote show origin
                                * remote origin
                                  Fetch URL: https://github.com/matao/DControl.git
                                  Push  URL: https://github.com/matao/DControl.git
                                  HEAD branch: master
                                  Remote branches:
                                    addSwitchDB tracked
                                    linechart   tracked
                                    master      tracked
                                    netflowData tracked
                                  Local branch configured for 'git pull':
                                    master merges with remote master
                                  Local refs configured for 'git push':
                                    master      pushes to master      (up to date)
                                    netflowData pushes to netflowData (up to date)

Removing and Renaming Remotes
    
    $ git remote rename dccontrol paul
    $ git remote
        origin
        paul

    $ git remote rm paul
    $ git remote
        origin  

Tags
    http://git-scm.com/book/en/Git-Basics-Tagging


Chapter 3 Branching

    each time you commit, a snapshot ( a SHA1-A ) will be created (for master or branch)
    $ git branch netflowData
    $ git checkout netflowData

        "Equals to  # git checkout -b netflowData"

    $ git commit -a -m ""

    switch back to master branch
    $ git checkout master
    $ git commit -a -m ""

    NOTE:
        HEAD is a pointer which points to the LOCAL branch you are currently working on

Merge your branch to master
    $ git checkout master
    $ git merge netflowData

    Then you can delete your branch
    $ git branch -d netflowData

    or you can merge your master to your branch
    $ git checkout netflowData
    $ git merge master

Merge conflict 
    http://git-scm.com/book/en/Git-Branching-Basic-Branching-and-Merging

Branch Management

    $ git branch
        * master
        netflowData
    NOTE: Notice the * character  indicates the branch that you currently have checked out

    $ git branch -v
    NOTE see the last commit on each branch,

    $ git branch --merged
          master
        * netflowData
    NOTE:  see which branches are already merged into the branch you’re on
     Branches on this list without the * in front of them are generally fine to delete with git branch -d; you’ve already incorporated their work into another branch, so you’re not going to lose anything.

     $ git branch --no-merged
     To see all the branches that contain work you haven’t yet merged in

Branching Workflows
    
Long-Running Branches

    http://git-scm.com/book/en/Git-Branching-Branching-Workflows

Remote Branches

    Remote branches are references to the state of branches on your remote repositories. They’re local branches that you can’t move; they’re moved automatically whenever you do any network communication. Remote branches act as bookmarks to remind you where the branches on your remote repositories were the last time you connected to them

    origin/master
    origin/netflowData

    This may be a bit confusing, so let’s look at an example. Let’s say you have a Git server on your network at git.ourcompany.com. If you clone from this, Git automatically names it origin for you, pulls down all its data, creates a pointer to where its master branch is, and names it origin/master locally; and you can’t move it. Git also gives you your own master branch starting at the same place as origin’s master branch, so you have something to work from (http://git-scm.com/book/en/Git-Branching-Remote-Branches)

    If you do some work on your local master branch, and, in the meantime, someone else pushes to git.ourcompany.com and updates its master branch, then your histories move forward differently. Also, as long as you stay out of contact with your origin server, your origin/master pointer doesn’t move 

    $ git fetch origin 
    NOTE:
        To synchronize your work, you run a git fetch origin command. This command looks up which server origin is (in this case, it’s git.ourcompany.com), fetches any data from it that you don’t yet have, and updates your local database, moving your origin/master pointer to its new, more up-to-date position

Pushing your branch to remote git repository

    When you want to share a branch with the world, you need to push it up to a remote that you have write access to. Your local branches aren’t automatically synchronized to the remotes you write to — you have to explicitly push the branches you want to share. That way, you can use private branches for work you don’t want to share, and push up only the topic branches you want to collaborate on.

    $ git push origin netflowData
    NOTES: it means: take my netflowData local branch and push it to update the remote's netflowData branch

    The next time one of your collaborators fetches from the server, they will get a reference to where the server’s version of serverfix is under the remote branch origin/netflowData
    IMPORTANT NOTES:
        It’s important to note that when you do a fetch that brings down new remote branches, you don’t automatically have local, editable copies of them. In other words, in this case, you don’t have a new netflowData branch. - you only have an origin/netlfowData pointer that your CANT modify
        
        $ git merge origin/netflowData (remote branch name)
        NOTES:
            this command will merge your netflowData branch to your current working branch.

        $git checkout -b netflowData origin/netflowData
        NOTES:
            this command will let you have your OWN LOCAL netflowData branch what you can work on. 

Tracking branches

    If you’re on a tracking branch and type git push, Git automatically knows which server and branch to push to. Also, running git pull while on one of these branches fetches all the remote references and then automatically merges in the corresponding remote branch.

    When you clone a repository, it generally automatically creates a master branch that tracks origin/master. That’s why git push and git pull work out of the box with no other arguments

    You can set up other tracking branches: git checkout -b [branch] [remotename]/[branch]
    ex: 
        $git checkout -b netflowData origin/netflowData
        OR.
        $ git checkout --track origin/netflowData

        Now your local branch netflowData will automatically push to and pull from origin/netflowData
        ex:
            Jack:DControl tonyalbums$ git branch
                * linechart
                  master
                  netflowData
        if we go git checkout linechart, then do git push/pull. Git will push/pull from origin/linechart

Delete Remote branches
    
    http://git-scm.com/book/en/Git-Branching-Remote-Branches

    Suppose you’re done with a remote branch — say, you and your collaborators are finished with a feature and have merged it into your remote’s master branch (or whatever branch your stable codeline is in). You can delete a remote branch using the rather obtuse syntax git push [remotename] :[branch]. If you want to delete your serverfix branch from the server, you run the following:

    $ git push origin :netflowData
    To git@github.com:schacon/simplegit.git
     - [deleted]         netflowData
     NOTES:
        after this, No more branch on your server. 

Rebasing

    http://git-scm.com/book/en/Git-Branching-Rebasing


    git log 


Chapter 4 Git on the server



Chapter 5 

Commit guildlines  (http://git-scm.com/book/en/Distributed-Git-Contributing-to-a-Project)

First check if there is any whitespace error
    $ git diff --check
Next, try to make each commit a logically separate changeset.
Last thing, commit with a message


Everytime you push to server, you need to do $ git fetch origin to find the difference (which you dont have it yet in your code)
And remember, in Git, you need to merge the commit locally first before you push to server

EX:
    $ git fetch origin
        From john@githost:simplegit
        + 049d078...fbff5bc master     -> origin/master
    NOTE:
        here now change is found at origin/master and now you have the referernce to that change,
        next you need to merge it to your own work
        $git merge origin/master
        Then do $ git commit -a -m ""

        THen test your code if it still works
        If it works, then $ git push origin master

        


Toturials from www.308tube.com/youtube/github

git init
git add .
git commit -a -m ""

git status
git log
git diff
git diff --cached

#create one repor at github.com

#use ssh to generate ssh key and upload at github.com
ssh-keygen -t ras -C "s.zhao.j@gmail.com"
#test connection from your pc
ssh -T git@github.com


#inside of your local repo, add a remote repo called origin (origin is a default name for the remote repo)
git remote add origin git@github.com:jackcrazy/youtube.demo.git
or your change origin to whatever name you like

# push local data into remote repo, called origin, also at master branch
git push origin master


branching
    all repo have a master
    you can create copies of your file using branck

    for a new branch, steps:
    create a local folder
    inside of the new folder, do "git clone git@github.com:jackcrazy/youtube.demo.git"
    now your have a copy of master branch in your local new folder

    inside your copy of branch, do "git log/status" to check commit history
    do "git branch" to check how many existing branches

    git branch # show all existing branches
    git branch newbranchname # create a new branch
    git checkout newbranchname # switch to that newbranch
    # or just use git checkout -b newbranchname

    Then setup a remote repo and push data to new the branch
    git remote add origin git@github.com:jackcrazy/youtube.demo.git
    git push origin "newbranchname"

    git checkout master # switch to master branch
    git push origin master

    at new branch:
        if you want to merge to master, just do git merge master. If there is any conflict, merge will fail. Fix the conflict and do a new commit again. 

    if master has changed, you need to get a new copy of files to your local file
        PULL: it is similar to a MERGE but PULL synchronizes your local repository with the remote repository
        
        git pull origin master
        # doing a pull, we have the most current master branch
        # now we can merge new release branch 
        at new branch you do can "git merge master" to merge with master branch code to your branch

    before you switch to different brance, you need to commit your current branch

    at master branch:
        "git merge yournewbranch"
        # now the yournewbranch is merged to your master branch
        then you need to "git push origin master" to push your remote repo
        also do "git push origin yournewbranch" to push your branch to remote repo

    when working in a team, Its always great to do a pull before your doing a push
    PULL - sync with GitHub
    PUSH - upload

    before you push, you did a PULL. If there is conflict, it will show you and you have to deal with it by yourself. Add you took care of the conflicts, you do:
        git add . 
        git commit -m "xxx"  
        git pull origin master ( or other branch you are working on)
        # if there is no more new data
        git push origin master

        
merging
cloning
forking



#############################################################

git delete a branch

git checkout -b newbranch
git push origin :newbranh # to delete this branch. notes the colon : is very important





















How to use githb
