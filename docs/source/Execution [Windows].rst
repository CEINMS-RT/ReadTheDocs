======================
Execution [Windows]
======================

.. _exe ref:

Modifiers and definitions
-------------------------

XML files
+++++++++

Now that CEINMS is installed and compiled, we need to create and define the parameters of the neuromusculoskeletal model.
Three examples are shown in the :ref:`Tutorials <Tutorial ref>`. The definitions of the simulation are defined in two **XML** files
that link to 3D models, connections, forces, loads, filters, etc. These **XML** files are called the subject and the execution file. \

Modifiers
+++++++++

Next to the XML files, there are a few modifiers available to the user, these are compiled in a table below:

+------------------------------------------------------------------------------+
|C:\\<PathToCeims-rt>\\bin\\Win\\Debug\\CEINMS.exe                             |
|[-g] [-p <string>] [-r <string>]                                              |
|[-v <int>] -e <string> -s <string>                                            |
|[--] [--version] [-h]                                                         |
+==============================================================================+
|Where:                                                                        |
+---------------+--------------------------------------------------------------+
|``-g``         |``--gui``                                                     |
+---------------+--------------------------------------------------------------+                                                                               
|Use the graphical interface                                                   |                            
+---------------+--------------------------------------------------------------+ 
|``-p <string>``|``--process <string>``                                        |
+---------------+--------------------------------------------------------------+                                
|Process the emgFilt.txt and ik.sto found in arg (string) directory in         |                                                                      
|a offline ways. This option overrule the execution.xml.                       |                                                        
+---------------+--------------------------------------------------------------+  
|``-r <string>``|``--record <string>``                                         |
+---------------+--------------------------------------------------------------+                               
|Save the output in a directory. The name of the directory is arg              |                                                                 
|(string).                                                                     |          
+---------------+--------------------------------------------------------------+  
|``-v <int>``   |``--verbose <int>``                                           |
+---------------+--------------------------------------------------------------+                          
|Verbose option. arg (int) is the level of verbose output (0 no output,        |                                                                       
|1 basic output, 2 debug information and 3 in-loop debug).                     |                                                          
+---------------+--------------------------------------------------------------+  
|``-e <string>``|``--execution <string>``                                      |
+---------------+--------------------------------------------------------------+                                  
|(required) Execution xml file option. See execution.xsd in XSD                |                                                               
|directory for more information.                                               |                                
+---------------+--------------------------------------------------------------+  
|``-s <string>``| ``--subject <string>``                                       |
+---------------+--------------------------------------------------------------+                                
|(required) Subject specific for CEINMS xml file. See subject.xsd in           |                                                                    
|XSD directory for more information.                                           |                                    
+---------------+--------------------------------------------------------------+  
|``-t <double>``|``--timer <double>``                                          |                                    
+---------------+--------------------------------------------------------------+                             
|(optional) Kill CEINMS & GUI after a given time (in seconds).                 |                                                              
+---------------+--------------------------------------------------------------+  
|``--``         |``--ignore_rest``                                             |                                    
+---------------+--------------------------------------------------------------+                  
|Ignores the rest of the labeled arguments following this flag.                |                                                               
+------------------------------------------------------------------------------+  
|``--version``                                                                 |                                    
+------------------------------------------------------------------------------+          
|Displays version information and exits.                                       |                                        
+---------------+--------------------------------------------------------------+  
|``-h``         |``--help``                                                    |                                    
+---------------+--------------------------------------------------------------+           
|Displays usage information and exits.                                         |                                      
+------------------------------------------------------------------------------+
