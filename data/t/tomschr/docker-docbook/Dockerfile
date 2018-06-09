# DOCKER-VERSION 1.1.0  
#  
FROM opensuse:42.1  
MAINTAINER Thomas Schraitle <toms@opensuse.org>  
  
# Add repositories  
RUN zypper ar -f
http://download.opensuse.org/repositories/Documentation:/Tools/openSUSE_Leap_42.1/Documentation:Tools.repo  
RUN zypper ar -f
http://download.opensuse.org/repositories/Publishing/openSUSE_Leap_42.1/Publishing.repo  
RUN zypper --non-interactive --gpg-auto-import-keys ref  
  
# Install packages  
RUN zypper in -y openSUSE-release sgml-skel lsb-release docbook_4 docbook_5
docbook-xsl-stylesheets docbook5-xsl-stylesheets geekodoc  
  
# ENTRYPOINT ["/bin/bash"]  

