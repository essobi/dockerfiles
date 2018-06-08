FROM fedora  
  
MAINTAINER David Makin <davidm@studioskylab.com>  
  
# Upgrade packages.  
RUN dnf -y upgrade \  
  
# Install "powerline" and other tools.  
# "which" is required by "powerline" (/usr/share/powerline/bash/powerline.sh).  
# "findutils" provides the "find" command.  
&& dnf -y install powerline which findutils tar git zip vim gcc-c++ make \  
  
# Setup npm  
&& curl --silent \--location https://rpm.nodesource.com/setup_6.x | bash - \  
&& dnf --nogpgcheck -y install nodejs \  
&& node install -g node-lambda \  
  
# Clean up.  
&& dnf -y clean all  
  
# Configure "powerline" theme so that it shows "git" branch info.  
ADD powerline.json /root/.config/powerline/config.json  
  
# Configure bash shell to use "powerline" by default.  
RUN printf '\n%s\n%s\n%s\n%s\n%s\n\n' '# Use powerline' 'powerline-daemon -q'
'POWERLINE_BASH_CONTINUATION=1' 'POWERLINE_BASH_SELECT=1' '.
/usr/share/powerline/bash/powerline.sh' >> ~/.bashrc  

