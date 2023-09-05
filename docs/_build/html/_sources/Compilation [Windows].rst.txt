======================
Compilation [Windows]
======================

.. _Compile ref:

Setup
-----

.. important:: Make sure the newest version of CEINMS is installed on your system before proceeding to this section.
    A guide to installing CEINMS can be found in the :ref:`Installation section <Download ref>`

.. _CMake ref:

CMake-GUI
+++++++++

During the installation process, CMake-GUI has been installed on your system. We will now use this software to create
a Visual Studio solution from which we can build the CEINMS executable. First, search for CMake-GUI by opening the Windows
search bar. this can be done by pressing the Windows key and typing "cmake". after finding CMake-GUI, open it. \

You will now be greeted with the GUI of CMake, At the top of the window are two important fields: \

``Where is the source code`` and ``Where to build the binaries``. \

These fields is where you fill in the CEINMS directories we downloaded earlier. For the example directory
``C:/Users/<NAME>/AppData/Local``, the source code is stored in the directory ``C:/Users/<NAME>/AppData/Local/CeinMS/ceinms-rt``.
The build directory can exist in the same folder, but it's recommended to add an extra directory layer like /build, which would make the build
directory ``C:/Users/<NAME>/AppData/Local/CeinMS/ceinms-rt/build``.

After defining these file paths, it's important to set the configuration of Cmake to create a solution for the right version of visual studio.
during the :ref:`installation <Installation ref>` of the dependencies, Visual Studio 2019 has been downloaded. click on the **Configure button**
and under **specify the generator for this project** choose **Visual Studio 16 2019**. keep the other options default for a normal 64-bit windows installation.
Press finish to complete

Once Cmake configures the solution, we can find the directory Glew has been installed in. normally, Glew is installed in the ``Program Files (x86)`` folder. \

In the Cmake search bar, search for Glew. six options will arise. the following options will require the corresponding entries: \

+-------------------------------+-------------------------------------------------------------+
|**Name**                       |Value                                                        |
+-------------------------------+-------------------------------------------------------------+
|**GLEW_INCLUDE_DIR**           |C:/Program Files (x86)/glew-2.1.0/include                    |
+-------------------------------+-------------------------------------------------------------+
|**GLEW_SHARED_LIBRARY_RELEASE**|C:/Program Files (x86)/glew-2.1.0/lib/Release/x64/glew32.lib |
+-------------------------------+-------------------------------------------------------------+
|**GLEW_STATIC_LIBRARY_RELEASE**|C:/Program Files (x86)/glew-2.1.0/lib/Release/x64/glew32s.lib|
+-------------------------------+-------------------------------------------------------------+

Now press generate and wait for the solution to be generated. \

once the generation is complete, press ``open project`` to open the project in Visual Studio. From here, on the right, there is a file tree with at the top ``ALL_BUILD``.
Right click this folder and press ``Build``. This will now build CEINMS. \

If any errors arise during this build, please refer to the :ref:`Troubleshooter <Trouble ref>`.