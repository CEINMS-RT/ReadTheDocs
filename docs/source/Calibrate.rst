===========
Calibration
===========

.. _Calibration ref:

Objective
---------
The objective of the calibration process is to find the optimal set of NMS model parameters, 
so that the digital twin will match the individual muscle and tendon
properties as closely as possible.
At the core of the calibration process is a simulated annealing algorithm.

Prerequisites
-------------
Before starting the calibration process, make sure to record one or more trials.
The recorded data should be stored in OpenSim storage format and named according to the following convention:

    * emg.sto: EMG data
    * ik.sto: kinematics data
    * id.sto: inverse dynamics data.
  
Use subfolders to organize multiple trials, for example:

    * run81/emg.sto
    * run81/ik.sto
    * run81/id.sto
    * walk36/emg.sto
    * walk36/ik.sto
    * walk36/id.sto.

Configuration
-------------

Calibration options and parameters are stored in a XML file.
The name and location of this file should be specified using the "-s" parameter (see example below).

.. tabs::

   .. code-tab:: s Windows

      .\bin\Win\Debug\calibrate.exe -e .\cfg\LowerLimbModel\executionRT.xml -s .\cfg\LowerLimbModel\Calibration.xml -g

   .. code-tab:: s Linux

      ./bin/Unix/calibrate -e ./cfg/LowerLimbModel/executionRT.xml -s ./cfg/LowerLimbModel/Calibration.xml -g

Calibration in CEINMS-RT is a two-step process:

    1. Spline computation: This step computes the muscle excitations from the EMG data using spline interpolation.  
    2. Simulated annealing: This step optimizes the NMS model parameters to minimize the difference between the simulated muscle excitations and the recorded EMG data.

The example command line shown above will execute *one* of the two steps, depending on the configuration specified in the XML file:

    * If the "use" parameter in the "computeSpline" section is set to "true", the program will execute the spline computation step.
    * If the "use" parameter in the "calibration" section is set to "true", the program will execute the simulated annealing step.

.. literalinclude:: /include/compute-spline.xml
    :language: xml
    :lines: 22,23,26-28,49
    :caption: Spline computation configuration.

.. literalinclude:: /include/Calibration.xml
    :language: xml
    :lines: 22,23,26-28,49
    :caption: Simulated annealing configuration.

