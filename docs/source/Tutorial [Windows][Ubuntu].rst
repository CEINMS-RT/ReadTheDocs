==========================
Tutorial [Windows][Ubuntu]
==========================

.. _Tutorial ref:

LowerLimbModel
--------------

Installation
++++++++++++

go to the respective github repository and download the LowerLimbModel folder as zip or use git checkout on the LowerLimbModel page to download the files on your local machine. 
Next, make sure :ref:`CEINMS is completely installed <Download ref>` and the cfg folder is in place. 
Once this is ready we can extract the contents of LowerLimbModel folder into the cfg folder. The folder might be suffixed -main, get rid of this part so the folder is called ``LowerLimbModel``.
in this LowerLimbModel folder should another folder called SplineCoeff which contains .bin files.
Move the SplineCoeff folder up one in the filetree so it's in the root of the cfg folder.

Usage
+++++

Using the LowerLimbModel is just like launching CEINMS normally, we only need to specify the right execution and subject xml in the run prompt and run the program.
for the LowerLimbModel, we use the executionRT.xml file and the subjectMTU.xml file. This will result in the following run command:

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e .\cfg\LowerLimbModel\executionRT.xml -s .\cfg\LowerLimbModel\subjectMTU.xml -g

What you will see is a skeleton on the right side of the screen and the emg data on the left.

BackModel
---------

Installation
++++++++++++

go to the respective github repository and download the BackModel folder as zip or use git checkout on the BackModel page to download the files on your local machine. 
Next, make sure :ref:`CEINMS is completely installed <Download ref>` and the cfg folder is in place. 
Once this is ready we can extract the contents of BackModel folder into the cfg folder. The folder might be suffixed -main, get rid of this part so the folder is called ``BackModel``.
in this BackModel folder should another folder called Spline coefficients which contains a .bin file rename this folder to SplineCoeff.
Move the SplineCoeff folder up one in the filetree so it's in the root of the cfg folder.

Usage
+++++

Using the BackModel is just like launching CEINMS normally, we only need to specify the right execution and subject xml in the run prompt and run the program.
for the BackModel, we use the executionRT.xml file and the lumbarModel_calibrated.xml file. This will result in the following run command:

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e ".\cfg\BackModel\Configuration files\executionRT.xml" -s ".\cfg\BackModel\CEINMS models\lumbarModel_calibrated.xml" -g

What you will see is a skeleton on the right side of the screen and the emg data on the left.

UpperLimbModel
--------------

Installation
++++++++++++

Download or clone the UpperLimbModel repository from the CEINMS github repository.
This tutorial is a way to show how to calibrate the models using the callibrate.exe. Make sure the repository is situated in the cfg folder
and there is a SplineCoeff folder in that same cfg folder as well.

Next, we are going to calibrate the model using calibrate.exe. 
This program takes similar perameters as CEINMS.exe, but for this example, 
the following command can be used:

.. code-block:: console

    .\bin\Win\Debug\calibrate.exe -e .\cfg\UpperLimbModel\ExecutionRT.xml -s .\cfg\UpperLimbModel\simulatedAnnealing.xml

After this, in the SplineCoeff folder, there should be a set of bin files called UpperLimbModel_Coefficients. 
these can then directly be used in the following section

Usage
+++++

Now that we created the spline coefficients, we can run CEINMS and witness our creation.
First however, we need the geometry files, normally these would be included in the github, 
but for this example we ask you to go to the simtk website `here <https://simtk.org/projects/upexdyn>`_ 
and to downoad the unimanual tutorial for opensim 4.1. from this tutorial zip, extract the geometry folder.
Now place the geometry folder in the UpperLimbModel folder so CEINMS can generate the proper 3D model. 
Now we can run the following command to run CEINMS with our own callibration.

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e .\cfg\UpperLimbModel\ExecutionRT.xml -s .\cfg\UpperLimbModel\Right_arm.xml -g

What you will see is a skeleton on the right side of the screen and the emg data on the left.
