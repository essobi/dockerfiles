FROM codenvy/ubuntu_gradle  
  
  
EXPOSE 8883 8443 443  
RUN sudo apt-get update && \  
echo Setup for non interactive installation prerequisite for apt-get && \  
# see https://goo.gl/J1oFMd for explanation of the next line  
# see also https://goo.gl/Ga8EZ8  
# set DEBIAN_FRONTEND in each command because ARG did not work and because of
this -> https://goo.gl/AE86Do  
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -q dialog  
  
RUN echo Installation and Setup of Python and PIP && \  
sudo DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
-q build-essential python2.7 python2.7-dev python-pip && \  
# If executing pip with sudo, you may want sudo's -H flag.  
sudo -H pip install -U pip && \  
# see https://goo.gl/Mscxfn for explanation of the next line  
sudo -H pip install -U setuptools && \  
sudo -H pip install virtualenv  
  
RUN echo Installation of awscli && \  
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -q groff && \  
sudo -H pip install awscli  
  
RUN echo Installation of ansible && \  
# see https://goo.gl/NWYxCC for ansible installation instructions  
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -q software-properties-
common && \  
sudo apt-add-repository ppa:ansible/ansible && \  
sudo apt-get update && \  
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -q ansible  
  
WORKDIR /projects  
  
CMD tail -f /dev/null  

