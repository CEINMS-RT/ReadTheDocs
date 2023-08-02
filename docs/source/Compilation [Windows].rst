======================
Compilation [Windows]
======================

.. _Compile ref:

Setup
-----

.. important:: Make sure the newest version of CEINMS is installed on your system before proceeding to this section.
    A guide to installing CEINMS can be found in the :ref:`Installation section <Download ref>`


CMake-GUI
+++++++++

During the installation process, CMake-GUI has been installed on your system. We will now use this software to create
a visual studio solution from which we can build the CEINMS executable. First, search for CMake-GUI by opening the windows
search bar. this can be done by pressing the windows key and typing "cmake". after finding CMake-GUI, open it. \

You will now be greeted with the GUI of CMake, At the top of the window are two important fields: \

``Where is the source code`` and ``Where to build the binaries``. \

These fields is where you fill in the CEINMS directories we downloaded earlier. For the example directory
``C:/Users/<NAME>/AppData/Local``, the source code is stored in the directory ``C:/Users/<NAME>/AppData/Local/CeinMS/ceinms-rt``.