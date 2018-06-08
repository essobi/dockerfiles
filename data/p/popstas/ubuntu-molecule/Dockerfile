FROM ubuntu:16.04  
  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y curl git wget  
  
# Install docker-engine  
RUN \  
apt-get install -y \--no-install-recommends apt-transport-https ca-
certificates software-properties-common && \  
curl -fsSL https://apt.dockerproject.org/gpg | apt-key add \- && \  
add-apt-repository "deb https://apt.dockerproject.org/repo/
ubuntu-$(lsb_release -cs) main" && \  
apt-get update && \  
apt-get -y install docker-engine  
  
# Install  
RUN \  
apt-get \--no-install-recommends -y install python python-apt python-pip
python-dev python-setuptools gcc libssl-dev libffi-dev && \  
pip install -U pip && \  
pip install molecule ansible docker && \  
pip uninstall -y pip && \  
apt-get purge -y python-apt python-pip python-dev gcc libssl-dev libffi-dev &&
\  
apt autoremove -y  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]

