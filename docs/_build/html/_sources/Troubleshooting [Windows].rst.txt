=========================
Troubleshooting [Windows]
=========================

.. _Trouble ref:

Downloading files
-----------------

When encountering isues downloading files from the repository, the following issues might occur: \

no access to the repository
+++++++++++++++++++++++++++

Solution\
 Make sure you have proper clearance to access the repository. If you don't have the necessary permissions,
 you won't be able to download files. Check with the repository administrators or owners to ensure that you have the required access rights.

Action\
 If further clearance is needed, you should contact the members of the repository and clarify your intentions for accessing the files. 
 Politely request additional clearance if required, explaining the purpose and reasons behind your request.

Note\
 Repositories often have specific access control mechanisms in place to protect sensitive or proprietary information. 
 Unauthorized access attempts may be flagged and could lead to account suspension or other penalties.

enter ssh passphrase
++++++++++++++++++++

Solution\
 If a password for the rsa ssh-key is already in place, try filling in the password. If the password does not get you through, you can change
 the password

Action\ 
 open a command terminal and navigating to ``C:/Users/<UserName>/.ssh`` with the ``cd`` command. After this, we change the password using the command:

 .. code-block:: cmd

    ssh-keygen -p -f id_rsa

 You will be prompted to enter the old passphrase, after the old passphrase, you will be prompted to enter a new passphrase.
 Repeat this new passphrase once more if you require to do so. Now, the passphrase has been updated.

Note\
 If the old password is unknown, there is no way to change or retieve this password. A new key must be requested or made.