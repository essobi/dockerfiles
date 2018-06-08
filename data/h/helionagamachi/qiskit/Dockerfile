FROM python:3.6.3  
  
# TODO: cleanup here?  
RUN apt-get update && \  
apt-get install -y sudo poppler-utils texlive-latex-base texlive-latex-extra  
  
  
RUN pip install --quiet qiskit jupyter  
  
ENV gid=1000 uid=1000  
  
# adds the group  
RUN groupadd -g $gid developer && \  
# creates the user named developer with the right uid and gid  
useradd -g $gid -u $uid -m developer && \  
# allow the developer user use sudo without a password  
echo "developer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
  
# default user to run commands on the container, also all RUN commands from
this point are executed  
# with this user  
USER developer  
  
# create the directory that will be used on the mount  
RUN mkdir /home/developer/app  
  
WORKDIR /home/developer/app  

