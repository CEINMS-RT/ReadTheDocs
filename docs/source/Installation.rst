============
Installation
============

.. _Installation:

Automatic installation [WINDOWS]
----------------------

If everything is download correctly, we can run the powershell script by running powershell in ``administrator`` mode.
This will open a new powershell terminal. Powershell can run with different clearance depending on the execution policy in place.
To view the execution policy, run the command

.. code-block:: powershell

   Get-ExecutionPolicy

in the terminal. Depening on the return, you may need to change your execution policy. To do this, simply run the command

.. code-block:: powershell

   Get-ExecutionPolicy UnRestricted

You might be prompted with a confirmation, to change the policy quickly, simply type ``A`` followed by ``Enter``. \
Next, move to the local installation folder like ``C:\Users\<NAME>\AppData\Local\ceinms-installer`` using the ``cd`` command
followed by the path specified above and press enter. \
Now, run the following command to start the installation process

.. code-block:: powershell

   ./installCEINMS.ps1

This will activate the powershell script and start installing CEINMS