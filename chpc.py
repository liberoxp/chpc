"""An user interface that allows user to directly change Houdini parameter callback script.
   An user interface, based on Houdini native UI script, that allows user to edit/rewrite 
   Houdini parameter callback script without opening "Edit Parameter Interface" window.
"""

import sys, os

import hou

gUI_FILE = '%s.ui' % os.path.splitext(__file__)[0]
gLANG_TO_INDEX = {'Hscript':0, 'Python':1}
gINDEX_TO_HOULANG = {0:hou.scriptLanguage.Hscript, 1:hou.scriptLanguage.Python}

global gDIALOG

def start():
    '''Mian Function.'''

    # Parse .ui file.
    global gDIALOG
    gDIALOG = hou.ui.createDialog(gUI_FILE)

    # Setup gadget callback functions.
    gDIALOG.addCallback('btn_getParmCallback.val', cb_btn_getParmCallback)
    gDIALOG.addCallback('btn_change.val', cb_btn_change)
    
    # Setup gadget values.
    cb_btn_getParmCallback()

    # Show dialog window.
    gDIALOG.setValue('dialog.val', True)

def cb_btn_change():
    '''Callback function called by "Change" button, and "start" function for initialization.'''
    
    parmPath = gDIALOG.value('strField_tarParm.val')
    parm = hou.parm(parmPath)
    if parm:
        script = gDIALOG.value('strField_newScript.val')
        langIdx = gDIALOG.value('menu_lang.val')
        
        if script:
            # Edit parameter template.
            templ = parm.parmTemplate()
            templ.setScriptCallback(script)
            templ.setScriptCallbackLanguage(gINDEX_TO_HOULANG[langIdx])

            # Replace parameter by edited template.
            parm.node().replaceSpareParmTuple(parm.name(), templ)

            # Update to old script string field.
            gDIALOG.setValue('strField_oldScript.val', script)
        else:
            hou.ui.displayMessage('Empty script, skip writing!', title='Change')
    else:
        hou.ui.displayMessage('Invalid parameter path!', title='Change')
  

def cb_btn_getParmCallback():
    '''Callback function called by "Get Parameter Callback info" button.'''
    
    title = 'Get Parameter Callback Info'

    path = getParmPath()
    if path:
        # Target parameter string field.
        gDIALOG.enableValue('strField_tarParm.val', True)
        gDIALOG.setValue('strField_tarParm.val', path)
        gDIALOG.enableValue('strField_tarParm.val', False)

        # Old script string field, and language menu item.
        script, lang = getCallbackInfo(path)
        gDIALOG.setValue('strField_oldScript.val', script)
        gDIALOG.setValue('menu_lang.val', gLANG_TO_INDEX[lang])
    else:
        hou.ui.displayMessage('No parameter copied!', title=title)

def getParmPath():
    '''Function used to get parameter info by checking internal parameter clipboard.'''
    
    contents = hou.parmClipboardContents()

    if contents:
        return contents[0].get('path')
    
    return None

def getCallbackInfo(parmPath):
    '''Function used to get callback information, such as script and language.'''

    parm = hou.parm(parmPath)
    parmTemp = parm.parmTemplate()
    
    script = parmTemp.scriptCallback()
    language = parmTemp.scriptCallbackLanguage().name()
    
    return (script, language)
