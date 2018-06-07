FROM fedora  
  
# Upgrade packages.  
RUN dnf -y upgrade  
  
# Install "powerline" and other tools.  
# "which" is required by "powerline" (/usr/share/powerline/bash/powerline.sh).  
# "findutils" provides the "find" command.  
RUN dnf -y install powerline which findutils tar wget  
  
# Clean up.  
RUN dnf -y clean all  
  
# Configure "powerline" theme so that it shows "git" branch info.  
ADD powerline.json /root/.config/powerline/config.json  
  
# Export the TERM environment variable.  
# Configure bash shell to use "powerline" by default.  
RUN printf '\n%s\n%s\n\n\n%s\n%s\n%s\n%s\n%s\n\n' '# Export TERM environment
variable' 'export TERM=xterm' '# Use powerline' 'powerline-daemon -q'
'POWERLINE_BASH_CONTINUATION=1' 'POWERLINE_BASH_SELECT=1' '.
/usr/share/powerline/bash/powerline.sh' >> ~/.bashrc  

