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

Calibration options and parameters are stored in an XML file.
The name and location of this file should be specified using the "-s" parameter (see example below).

.. code-block:: console

    .\bin\Win\Debug\calibrate.exe -e .\cfg\LowerLimbModel\executionRT.xml -s .\cfg\LowerLimbModel\Calibration.xml

Calibration in CEINMS-RT is a two-step process:
    1. Spline computation: This step computes the muscle excitations from the EMG data using spline interpolation.  
    2. Simulated annealing: This step optimizes the NMS model parameters to minimize the difference between the simulated muscle excitations and the recorded EMG data.

.. literalinclude:: /include/Calibration.xml
    :language: xml
    :lines: 31-33
    :caption: Example of DOFs to calibrate in the config file.

.. tabs::

   .. code-tab:: c

         C Main Function

   .. code-tab:: c++

         C++ Main Function

   .. code-tab:: py

         Python Main Function

   .. code-tab:: java

         Java Main Function

   .. code-tab:: julia

         Julia Main Function

   .. code-tab:: fortran

         Fortran Main Function

   .. code-tab:: r R

         R Main Function

.. tabs::

   .. code-tab:: c

         int main(const int argc, const char **argv) {
         return 0;
         }

   .. code-tab:: c++

         int main(const int argc, const char **argv) {
         return 0;
         }

   .. code-tab:: py

         def main():
            return

   .. code-tab:: java

         class Main {
            public static void main(String[] args) {
            }
         }

   .. code-tab:: julia

         function main()
         end

   .. code-tab:: fortran

         PROGRAM main
         END PROGRAM main

   .. code-tab:: r R

         main <- function() {
            return(0)
         }
