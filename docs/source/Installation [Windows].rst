======================
Installation [Windows]
======================

.. _Download ref:

Downloading files
+++++++++++++++++

Before we can install CEINMS, we need to get all the required files for installation.
These can be found on GitHub. In order to download this repository
without any issues, we will use Git to clone the repository onto our local machine.
Make sure there is a recent version of `Github desktop <https://desktop.github.com/>`_
with `Git Bash <https://www.atlassian.com/git/tutorials/git-bash>`_ installed. Now, open
Git Bash so we can start the installation. \

Move to a local folder like ``C:\Users\<NAME>\AppData\Local\CeinMS`` using the ``cd`` command
followed by the path specified above and press enter. \
You may experience Git Bash telling you there is no such path available. \
For this error message, the fix might be to change the direction of the slash. \
This will result in a file path like ``C:/Users/<NAME>/AppData/Local/CeinMS``.

Now clone the `CEINMS installer <https://github.com/CEINMS-RT/CEINMS-RT_Installer>`_ repository 
by clicking the ``clone`` button and pressing the copy button or copying

.. code-block:: bash

   git clone git@github.com:CEINMS-RT/CEINMS-RT_Installer.git

After entering this code, Git Bash might ask for the passcode to the SSH key connected to GitHub,
Simply enter the passcode and the installation will proceed. Now, if we take a look in the folder,
we find a new folder entry called ``ceinms-installer``. Inside are all the dependencies required
and a powershell script called ``installCEINMS.ps1``.

.. _Installation ref:

Automatic installation
++++++++++++++++++++++

Now that everything is download correctly, we can run the powershell script by running powershell in ``administrator`` mode.
This will open a new powershell terminal. Powershell can run with different clearance depending on the execution policy in place.
To view the execution policy, run the command

.. code-block:: powershell

   Get-ExecutionPolicy

In the terminal. Depening on the return, you may need to change your execution policy. To do this, simply run the command

.. code-block:: powershell

   Get-ExecutionPolicy UnRestricted

You might be prompted with a confirmation, to change the policy quickly, simply type ``A`` followed by ``Enter``. \
Next, move to the local installation folder like ``C:\Users\<NAME>\AppData\Local\CeinMS\ceinms-installer`` using the ``cd`` command
followed by the path specified above and press enter. \
Now, run the following command to start the installation process

.. code-block:: powershell

   ./installCEINMS.ps1

This will activate the powershell script and start installing CEINMS. You can keep track of any errors that may occur
during the installation process, frequently encountered error messages and their corresponding fixes are listed
in the :ref:`Troubleshooter <Trouble ref>`. If the installation goes on without issues, you should be greeted with a directory
selection window issuing you to select the output directory of the source code. This can be the same as the directory
used when downloading the installer; namely, ``C:\Users\<NAME>\AppData\Local\CeinMS``. This will create a new folder in that directory
named ceinms-rt in which the source files are stored, we will use this folder during :ref:`compilation <Compile ref>`.