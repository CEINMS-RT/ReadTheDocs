============
Installation
============

.. _Download ref:

Downloading files
+++++++++++++++++

For an up to date `README <https://github.com/CEINMS-RT/CEINMS-RT_Installer/blob/master/README.md>`_ 
please follow the provided link. 

Before we can install CEINMS-RT, we need to get all the required files for
installation.
From the installer repo's `homepage <https://github.com/CEINMS-RT/CEINMS-RT_Installer>`_ on GitHub, 
click on the green ``Code`` button, and then copy the clone url to the clipboard.
Clone the repository to a location of your choice.
After cloning you will find all the dependencies required and a PowerShell script called 
``installCEINMS.ps1``.

.. _Installation ref:

Automatic installation
++++++++++++++++++++++

Now that everything is download correctly, we can run the PowerShell script 
by running PowerShell in ``administrator`` mode.
This will open a new PowerShell terminal. PowerShell can run with different 
clearance depending on the execution policy in place.
To view the execution policy, run the command:

.. code-block:: powershell

   Get-ExecutionPolicy

Depending on the return, you may need to change your execution policy. To do 
this, simply run the command:

.. code-block:: powershell

   Set-ExecutionPolicy UnRestricted

| You might be prompted with a confirmation, to change the policy quickly, simply type ``A`` followed by ``Enter``.
| Next, move to the local installation folder using the ``cd`` command. Now, run the following command to start the installation process:

.. code-block:: powershell

   ./installCEINMS.ps1

This will activate the PowerShell script.
As a first step all CEINMS-RT dependencies will be installed.
You can keep track of any errors that may occur 
during the installation process.
Frequently encountered error messages and their corresponding fixes are listed
in the :ref:`Troubleshooting <Trouble ref>` section.
If the installation goes on without issues, you should be greeted with a directory
selection window issuing you to select the output directory of the source code.
The installation script will create a new folder in the designated directory
named ``ceinms-rt`` in which the source files are stored.
We will use this folder in the :ref:`Compilation <Compile ref>` section.
As a final step the PowerShell script will compile the core of CEINMS-RT.