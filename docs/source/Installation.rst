============
Installation
============

.. _Installation:

Automatic installation [WINDOWS]
----------------------
Before we can install CEINMS, we need to get all the required files for installation.
These can be found on the bitbucket repository. In order to download this repository
without any issues, we will use git to clone the repository onto our local machine.
make sure there is a recent version of `github desktop <https://desktop.github.com/>`_
with `git bash <https://www.atlassian.com/git/tutorials/git-bash>`_ installed. Now, open
git bash so we can start the installation. \

move to a local folder like ``C:\Users\<NAME>\AppData\Local`` using the ``cd`` command
followed by the path specified above and press enter. \

Now clone the `CEINMS installer <https://bitbucket.org/ctw-bw/ceinms-installer/src/master/>`_ repository 
by clicking the ``clone`` button and pressing the copy button or copying

.. code-block:: txt

   git clone git@bitbucket.org:ctw-bw/ceinms-installer.git

After entering this code, git bash might ask for the passcode to the ssh key connected to bitbucket,
Simply enter the passcode and the installation will proceed. Now, if we take a look in the folder,
we find a new folder entry called ``ceinms-installer``. inside are all the dependencies required
and a powershell script called ``installCEINMS.ps1``.