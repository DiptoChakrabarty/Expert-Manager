# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

/usr/sbin/sshd -f /etc/ssh/sshd_config

/usr/sbin/shellinaboxd -u shellinabox -g shellinabox --cert=/var/lib/shellinabox --port=4200 &
