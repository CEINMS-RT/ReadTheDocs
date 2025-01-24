========
Tutorial
========

.. _Tutorial ref:

LowerLimbModel
--------------

Installation
++++++++++++

Go to the respective GitHub `repository <https://github.com/CEINMS-RT/LowerLimbModel>`_. 
Click on the green ``Code`` button, and then select ``Download ZIP``. Next, make sure :ref:`CEINMS is completely installed <Download ref>` 
and the ``cfg`` folder is in place. Once this is ready we can extract the zip file into the ``cfg`` folder. 
If the folder is suffixed "-main", get rid of this part so the folder is called ``LowerLimbModel``.
The ``LowerLimbModel`` folder should contain a subfolder called ``SplineCoeff`` with .bin files.

.. important:: 
   Move the ``SplineCoeff`` folder one level up in the filetree so it's in the root of the ``cfg`` folder.

Usage
+++++

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e .\cfg\LowerLimbModel\executionRT.xml -s .\cfg\LowerLimbModel\data\subjectCalibration.xml -p cfg\LowerLimbModel\data\run81  -g

You should see a window with on the left side EMG data and on the right side a running skeleton.

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e .\cfg\LowerLimbModel\executionRT.xml -s .\cfg\LowerLimbModel\data\subjectCalibration.xml -p cfg\LowerLimbModel\data\walk36  -g

You should see a window with on the left side EMG data and on the right side a walking skeleton.

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e .\cfg\LowerLimbModel\executionRT.xml -s .\cfg\LowerLimbModel\data\subjectCalibration.xml -p cfg\LowerLimbModel\data\walk45  -g

You should see a window with on the left side EMG data and on the right side a walking skeleton.

BackModel
---------

Installation
++++++++++++

Go to the respective GitHub `repository <https://github.com/CEINMS-RT/BackModel>`_. 
Click on the green ``Code`` button, and then select ``Download ZIP``. Next, make sure :ref:`CEINMS is completely installed <Download ref>` 
and the ``cfg`` folder is in place. Once this is ready we can extract the zip file into the ``cfg`` folder. 
If the folder is suffixed "-main", get rid of this part so the folder is called ``BackModel``.
The ``BackModel`` folder should contain a subfolder called ``Spline coefficents`` with .bin files.

.. important:: 
   * Rename the ``Spline coefficents`` folder to ``SplineCoeff`` and move it one level up in the filetree so it's in the root of the ``cfg`` folder.
   * Copy the contents of folder ``cfg\BackModel\Geometry`` to folder ``cfg\BackModel\OpenSim model``.

Usage
+++++

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e "cfg\BackModel\Configuration files\executionRT.xml" -s "cfg\BackModel\CEINMS models\lumbarModel_calibrated.xml" -p "cfg\BackModel\Sample data\squat5kg" -g

You should see a window with on the left side EMG data and on the right side a squating skeleton.

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e "cfg\BackModel\Configuration files\executionRT.xml" -s "cfg\BackModel\CEINMS models\lumbarModel_calibrated.xml" -p "cfg\BackModel\Sample data\squat15kg" -g

You should see a window with on the left side EMG data and on the right side a squating skeleton.

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e "cfg\BackModel\Configuration files\executionRT.xml" -s "cfg\BackModel\CEINMS models\lumbarModel_calibrated.xml" -p "cfg\BackModel\Sample data\stoop5kg" -g

You should see a window with on the left side EMG data and on the right side a stooping skeleton.

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e "cfg\BackModel\Configuration files\executionRT.xml" -s "cfg\BackModel\CEINMS models\lumbarModel_calibrated.xml" -p "cfg\BackModel\Sample data\stoop15kg" -g

You should see a window with on the left side EMG data and on the right side a stooping skeleton.

UpperLimbModel
--------------

Installation
++++++++++++

Go to the respective GitHub `repository <https://github.com/CEINMS-RT/UpperLimbModel>`_. 
Click on the green ``Code`` button, and then select ``Download ZIP``. Next, make sure :ref:`CEINMS is completely installed <Download ref>` 
and the ``cfg`` folder is in place. Once this is ready we can extract the zip file into the ``cfg`` folder. 

.. important:: 
   Make sure the folder ``cfg\SplineCoeff`` is present.

Calibrate
+++++++++

Next, we are going to calibrate the model using ``calibrate.exe``:

.. code-block:: console

    .\bin\Win\Debug\calibrate.exe -e .\cfg\UpperLimbModel\executionRT.xml -s .\cfg\UpperLimbModel\simulatedAnnealing.xml

After execution the folder ``cfg\SplineCoeff`` will contain files named ``UpperLimbModel_Coefficients_[0-3].bin``.

Usage
+++++

Now that we created the spline coefficients, we can run CEINMS-RT and witness our creation:

.. code-block:: console

    .\bin\Win\Debug\CEINMS.exe -e .\cfg\UpperLimbModel\ExecutionRT.xml -s .\cfg\UpperLimbModel\Right_arm.xml -g

You should see a window with on the left side EMG data and on the right side a skeleton with only a right arm.
