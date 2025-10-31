============
Repositories
============

.. _Repositories ref:

Source Code
-----------

* `Core <https://github.com/CEINMS-RT/ceinmsrt-core-cpp>`_
* `Delsys Plugin <https://github.com/CEINMS-RT/ceinmsrt-plugin-delsys-cpp>`_
* `EMG UDP Plugin <https://github.com/CEINMS-RT/ceinmsrt-plugin-emgudp-cpp>`_
* `Moticon Plugin <https://github.com/CEINMS-RT/ceinmsrt-plugin-moticon-cpp>`_
* `RTOSIM Plugin <https://github.com/CEINMS-RT/ceinmsrt-plugin-rtosim-cpp>`_
* `ROS Plugin <https://github.com/CEINMS-RT/ceinmsrt-plugin-ros-cpp>`_
* `TwinCAT Plugin <https://github.com/CEINMS-RT/ceinmsrt-plugin-twincat-cpp>`_
* `TwinCAT EMG PLugin <https://github.com/CEINMS-RT/ceinmsrt-plugin-twincatemg-cpp>`_
* `UDP Plugin <https://github.com/CEINMS-RT/ceinmsrt-plugin-udp-cpp>`_
* `Xsens Plugin <https://github.com/CEINMS-RT/ceinmsrt-plugin-xsens-cpp>`_

Models
------

* `Back Model <https://github.com/CEINMS-RT/BackModel>`_
* `Lower Limb Model <https://github.com/CEINMS-RT/LowerLimbModel>`_
* `Upper Limb Model <https://github.com/CEINMS-RT/UpperLimbModel>`_

Plugin Templates
----------------

* `Sample EMG & Angle <https://github.com/CEINMS-RT/ceinmsrt-plugin-sample-emg-angle-cpp>`_
* `Sample Angle, EMG & Consumer <https://github.com/CEINMS-RT/ceinmsrt-plugin-sample-angle-emg-consumer-cpp>`_
* `Sample Angle & Consumer <https://github.com/CEINMS-RT/ceinmsrt-plugin-sample-angle-consumer-cpp>`_


Read The Docs
----------------
If you wish to build the documentation locally, you can do the following steps:

Clone the ReadTheDocs repository: 

.. code-block:: console

    git clone https://github.com/CEINMS-RT/ReadTheDocs.git


Go to the doc/ directory:

.. code-block:: console

    cd ReadTheDocs/docs


Install the dependencies: 

.. code-block:: console

    pip install -r requirements.txt

Build the HTML: 

.. code-block:: console

    make html

Navigate to the build folder and open build/html/index.html in a browser.