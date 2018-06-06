FROM ubuntu:14.04.3  
# Update system packages  
RUN apt-get clean && \  
apt-get update && \  
apt-get -y upgrade  
  
RUN apt-get update && apt-get install -y \  
wget \  
python \  
unzip  
  
WORKDIR /tmp  
  
# Install a specific version of docker  
RUN wget "https://get.docker.com/builds/Linux/x86_64/docker-1.8.3" -O
/usr/local/bin/docker && \  
chmod +x /usr/local/bin/docker  
  
# Install AWS CLI Client so we can push the deployment  
RUN wget "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -O awscli-
bundle.zip && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
# Install jq  
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O
/usr/local/bin/jq && \  
chmod +x /usr/local/bin/jq  
  
COPY . /usr/src/docker-builder  
WORKDIR /usr/src/docker-builder  
  
EXPOSE 5000  
CMD ./build.sh  

