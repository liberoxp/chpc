CHPC
====

aka Change Houdini Parameter Callback, is a tool that allows Houdini user to add/edit callback script of a **spare(extra) parameter** in Python or Hscript directly without opening "Edit Parameter Interface" window and wasting time on searching parameter.

![chpc_gui](https://raw.github.com/liberoxp/chpc/master/pic/chpc_main_window.png)

System requirements
-------------------
This tool requires Python2.6 or later to run and has been tested well in Houdini13.0.314 for Mac OSX(Mavericks).

This tool won't deal any thing with local file system, and since it is based on [HDK ui scripting](http://www.sidefx.com/docs/hdk13.0/_h_d_k__u_i_native__u_i_script.html), it should be able to work on either Windows or Linux.

How to install?
---------------
Download this tool from https://github.com/liberoxp/chpc/archive/master.zip and extract.

Copy **chpc.py** and **chpc.ui** to wherever Houdini can search for in you environment.

i.e. $HOME/Library/Preferences/houdini/13.0/scripts/python -- Mac OSX

How to integrate into Houdini environment?
-----------
Once this tool can be found in the Python search paths, user can load it by opening Python shell in Houdini to import **chpc** module, then invoke its **start()** function.
```
import chpc
chpc.start()
```
One can write a shelf tool with this code snippet to get a straight forward sense of using it.

How to use it?
-------------------------------
Simply just choose a **spare parameter**(may have a callback script written or need to add callback script) and copy it(to parameter clipboard), then execute this tool.

![copy_parameter](https://raw.github.com/liberoxp/chpc/master/pic/copy_parameter.png)


If you forgot to copy parameter and executed this tool right away, a warning message will pop-up. Don't worry, Just click **OK** to close this message, the main window will show up.

![no_parameter_copied](https://raw.github.com/liberoxp/chpc/master/pic/no_parameter_copied.png)

In this case you don't need to close the main window to restart, just copy the parameter you want, then press **Get parameter callback info** button. You will see the **Target parameter** text field is filled by the correct parameter path and its callback information will be shown in the main window. 

![get_parameter_callback_info](https://raw.github.com/liberoxp/chpc/master/pic/get_parameter_callback_info.png)

Once the **New script** text field and the **Language** drop-down menu are all set, press the **Change** button to write the new callback information to the parameter.

![new_script_and_change_button](https://raw.github.com/liberoxp/chpc/master/pic/new_script_and_change_button.png)

If you left the **New script** text field empty and pressed **Change** button, another warning message will pop-up. 

![empty_script](https://raw.github.com/liberoxp/chpc/master/pic/empty_script.png)

Output Message and Workflow
---------------------------
Once pressing **Change** button, a message will be output on the Python shell screen. The output message indicates **when** and **which** parameter was changed by **what** kind of information.

The main window will not close after pressing **Change** button, this way you can keep on changing callback script without re-running this tool till it gets you the right result.

![output_log](https://raw.githubusercontent.com/liberoxp/chpc/master/pic/output_log.png)

**PS**. The previous version of this tool (based on PyQt4) is stored at [Google Code](https://code.google.com/p/change-houdini-parameter-callback).
