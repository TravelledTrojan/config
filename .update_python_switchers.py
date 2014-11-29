#!/usr/bin/env python

import os

def detectPythonVersions(python_frameworkPath):
    root = os.path.join(python_frameworkPath, 'Versions')
    if not os.path.isdir(root):
        return []
    versions = [v for v in os.listdir(root)
            if not os.path.islink(os.path.join(root, v))]
    return versions
    
def generate_bash_select_func(frameworkPath, installType, version):
    values = {
        'frameworkPath': frameworkPath,
        'installType': installType,
        'version': version,
        'stripped_version': version.replace(".", ""),
        }
    bashFunctionTitle = 'setpy{stripped_version}'.format(**values)
    values['pythonPath'] = '{frameworkPath}/Versions/{version}/bin/'.format(**values)
    bashFunction = """
        setpy{stripped_version}()
        {{
            PATH=\"{pythonPath}:${{ORIGINAL_PATH}}\"
            export PATH
            update_prompt {installType}{version}
        }}
        \n""".format(**values)
    functionDescription = (bashFunctionTitle, values['pythonPath'])
    return functionDescription, bashFunction

def generate_bash_select_functions(outFn, frameworkPath, installType):
    for v in detectPythonVersions(frameworkPath):
        functionDescription, bashFunction = generate_bash_select_func(frameworkPath, installType, v)
        yield functionDescription
        outFn(bashFunction)

def generateBashFunctionIndex(outFn, functionDescriptions):
    outFn('setpy()\n{\n')
    for ft in functionDescriptions:
        outFn('\techo " * %s -> %s"\n' % ft)
    outFn('}\n')

if __name__ == '__main__':
    SYSTEM_ROOT = "/System/Library/Frameworks/Python.framework"
    MACPYTHON_ROOT = "/Library/Frameworks/Python.framework"

    outname = os.path.expandvars("$HOME/.python_switchers.bash")
    outfile = open(outname, 'w+')

    f1 = generate_bash_select_functions(outfile.write, SYSTEM_ROOT, 'Python')
    f2 = generate_bash_select_functions(outfile.write, MACPYTHON_ROOT, 'MacPython')
    functionTitles = [ f for f in f1]
    map(functionTitles.append, f2)
    functionTitles.sort()
    generateBashFunctionIndex(outfile.write, functionTitles)

    outfile.close()
