FROM jenkins/jenkins:lts  
  
MAINTAINER Kamran Kashef  
  
USER root  
  
RUN apt-get update && apt-get -y upgrade && \  
apt-get install -y vim ruby \  
python-pip python-dev build-essential && \  
cd /opt && \  
curl -O https://s3.amazonaws.com/deployment-pack/opt-pack.zip && \  
unzip opt-pack.zip && \  
rm -rf opt-pack.zip && \  
mv bashrc oldbashrc && \  
cat oldbashrc | grep opt | sed -e 's/~//' > bashrc && \  
cat bashrc && \  
mv opt/* .&& \  
rm oldbashrc && \  
rmdir opt && \  
pip install --upgrade pip && \  
pip install awscli --upgrade --user && \  
pip install awscli --upgrade --user  
  
RUN cd /bin && \  
curl -O https://kliplink.com/kl && \  
chmod +x kl  
  
RUN apt-get install -y p7zip  

