FROM fedora:rawhide  
  
#  
RUN dnf -q -y update  
RUN dnf -q -y install git wget python wine  
RUN dnf -q -y install mingw32-qt5-*  
RUN dnf -q -y install mingw64-qt5-*  
  
#  
RUN mkdir -p /opt/qt59/bin/  
RUN git clone
https://skiter@bitbucket.org/snippets/skiter/89Edqn/qt59-envsh.git
/opt/qt59/bin/.  
RUN chmod +x /opt/qt59/bin/qt59-env.sh

