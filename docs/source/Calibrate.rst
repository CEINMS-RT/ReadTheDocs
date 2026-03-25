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

Calibration in CEINMS-RT is a two-step process:
    1. Spline computation: This step computes the muscle excitations from the EMG data using spline interpolation.  
    2. Simulated annealing: This step optimizes the NMS model parameters to minimize the difference between the simulated muscle excitations and the recorded EMG data.

Calibration options and parameters can be found in the config file, for example which DOFs to calibrate (see example below).

.. code-block:: console

    .\bin\Win\Debug\calibrate.exe -e .\cfg\LowerLimbModel\executionRT.xml -s .\cfg\LowerLimbModel\Calibration.xml

.. literalinclude:: /include/Calibration.xml
    :language: xml
    :lines: 31-33
    :caption: Example of DOFs to calibrate in the config file.
