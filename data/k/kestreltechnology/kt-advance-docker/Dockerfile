# A Docker container shell for supporting KT Advance Analyzer under Linux  
FROM centos:latest  
MAINTAINER "Matt Barry" mrbarry@kestreltechnology.com  
  
## Add packages for KT Advance evaluation to a basic Centos 7 platform  
RUN yum update -y \  
&& yum group install -y "Development Tools" \  
&& yum install -y \  
cmake \  
lit \  
ocaml ocaml-findlib \  
java-1.8.0-openjdk \  
sudo \  
which \  
emacs \  
vim \  
epel-release python-pip  
  
## Build Bear from source  
# ADD Bear*.zip bear*.sh /home/bear/  
ADD bear*.sh /home/bear/  
WORKDIR /home/bear  
RUN chmod a+x /home/bear/*.sh  
# run separately to avoid open file busy  
RUN /home/bear/bear-build.sh  
  
## Create a user  
RUN useradd --create-home --shell /bin/bash ktuser \  
&& echo 'ktuser:ktuser' | chpasswd \  
&& usermod -aG wheel ktuser  
  
USER ktuser  
WORKDIR /home/ktuser  
  
## expect user to clone GitHub repo at /home to it appears as /home/ktadvance  
ENV PYTHONPATH=/home/ktuser/ktadvance  

