# Nice Coloring for prompt
# Black       0;30     Dark Gray     1;30
# Blue        0;34     Light Blue    1;34
# Green       0;32     Light Green   1;32
# Cyan        0;36     Light Cyan    1;36
# Red         0;31     Light Red     1;31
# Purple      0;35     Light Purple  1;35
# Brown       0;33     Yellow        1;33
# Light Gray  0;37     White         1;37

# Enable `ls` usage of colors
export CLICOLOR=1

export GITHUB=https://github.com/TravelledTrojan

# Nice Coloring for prompt with a special tag
update_prompt() {
    baseprompt="\[\e[0;32m\]\u\[\e[m\]\[\e[1;34m\]@\[\e[m\]\[\e[0;32m\]\h\[\e[m\]"
    workingdir="\[\e[1;34m\]\w\[\e[m\]"
    promptchar="\[\e[0;32m\]\$\[\e[m\]"
    if [ "$1" == "" ]
    then
        localtag=""
    else
        localtag=" \[\e[m\]\[\e[0;33m\]$1\[\e[m\]"
    fi
    export PS1="($baseprompt$localtag) $workingdir $promptchar "
}

export ORIGINAL_PATH=$PATH
update_prompt
$HOME/.update_python_switchers.py
source $HOME/.python_switchers.bash
rm $HOME/.python_switchers.bash
