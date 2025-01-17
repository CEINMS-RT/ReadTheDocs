======================
Installation [Ubuntu]
======================

.. _Installation-Ubuntu ref:
.. code-block:: shell-session

   sudo apt-get install cmake-gui libboost-all-dev xsdcxx qtbase5-dev libglew-dev git g++ libblas-dev liblapack-dev libxerces-c-dev libtbb-dev freeglut3-dev libeigen3-dev libboost-all-dev

If the Ubuntu version is too old and Boost version is < 1.68, do the following:

.. code-block:: shell-session

   sudo apt-get remove libboost-all-dev
   sudo add-apt-repository ppa:mhier/libboost-latest
   sudo apt update
   sudo apt autoremove
   sudo apt install libboost1.71-dev

You have to install `Pagmo2 <https://esa.github.io/pagmo2/install.html#installation-from-source>`_ from source.
For the compilation use the following commands:

.. code-block:: shell-session

   cmake ../ -DPAGMO_BUILD_TESTS=OFF -DCMAKE_INSTALL_PREFIX=~/.local -DPAGMO_WITH_EIGEN3=ON
   cmake --build .
   cmake --build . --target install

For compiling `Opensim <https://github.com/opensim-org/opensim-core/tree/4.3>`_ clone with Git:

.. code-block:: shell-session

   git clone https://github.com/opensim-org/opensim-core.git
   cd opensim-core
   git checkout tags/4.3

Follow this step: https://github.com/opensim-org/opensim-core#on-ubuntu-using-unix-makefiles

For compilation of Dependencies select: ``docopt``, ``simbody`` and ``spdlog`` and set CMAKE_BUILD_TYPE to ``Debug`` for easier debugging later.