FROM ubuntu:17.10  
ENV KUBECTL_VERSION v1.9.4  
ENV DOCKER_VERSION 17.12.1-ce  
  
#  
# This container has docker, kubectl, ansible and molecule in it.  
#  
RUN apt-get update && apt-get install -y \  
bash \  
curl \  
git \  
python \  
python-pip \  
build-essential \  
apt-transport-https \  
ca-certificates \  
software-properties-common \  
vim  
  
RUN pip install --upgrade \  
pip \  
setuptools \  
ansible \  
molecule \  
awscli  
  
# Installing kubectl don't forget you are going to need a kubeconfig  
RUN curl -LO https://storage.googleapis.com/kubernetes-
release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl  
RUN chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl  
  
# Download and place the docker binary file.  
RUN curl -LO
https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz
&& \  
tar zxf docker-${DOCKER_VERSION}.tgz && \  
chmod +x docker/docker && \  
mv docker/docker /usr/local/bin/  
  
# add a normal user such as drone  
RUN groupadd -g 999 drone  
RUN useradd -r -m -g drone -u 999 drone  
  
#Add user to docker group  
#RUN usermod -aG docker drone  
# If we want to run the docker command we expect to have the socket mounted  
VOLUME /var/lib/docker  
# Allow a user directory to be mounted  
VOLUME /home/drone  
  
# change to the user drone  
USER drone  

