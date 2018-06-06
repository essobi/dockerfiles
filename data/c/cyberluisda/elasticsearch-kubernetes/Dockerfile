FROM cyberluisda/elasticsearch-kubernetes:5.6.2  
MAINTAINER Luis David Barrios (cyberluisda@gmail.com)  
  
#ADDING default ES_HOME  
ENV ES_HOME /elasticsearch  
# Install plugins (NODE_NAME is mandatory by default use uuidgen)  
RUN yes | \  
NODE_NAME="${NODE_NAME:-$(uuidgen)}" \  
bin/elasticsearch-plugin install --batch x-pack  
  
# Software required  
RUN \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
unzip \  
iproute2 \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add certificate-selfsigned  
ADD files/* ${ES_HOME}/thirdparty/  
RUN chmod a+x ${ES_HOME}/thirdparty/certificates-selfigned.sh  
  
# Active certificates-selfsigned.sh patching file  
RUN patch -i ${ES_HOME}/thirdparty/active-certificates-selfsigned.patch
${ES_HOME}/thirdparty/pre-configure.sh  

