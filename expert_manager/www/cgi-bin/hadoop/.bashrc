# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias d='date'


#welcome message


# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi


#provide java path [permanent]
export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/
export PATH=/usr/java/jdk1.8.0_171-amd64//bin/:$PATH


