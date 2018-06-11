FROM openwhisk/controller  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get install -y \  
git \  
curl \  
sudo \  
python-pip  
  
RUN git clone https://github.com/openwhisk/openwhisk /openwhisk  
RUN /openwhisk/tools/ubuntu-setup/ansible.sh  
  
RUN curl -L https://github.com/apache/incubator-openwhisk-
cli/releases/download/latest/OpenWhisk_CLI-latest-linux-amd64.tgz | tar xz &&
mv wsk /openwhisk/bin/wsk  
  
COPY controller-init.sh /init.sh  
  
ENTRYPOINT ["/bin/bash", "/init.sh"]  

