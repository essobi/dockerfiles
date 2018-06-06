FROM debian:jessie  
MAINTAINER Ryan Grieve <ryan@rehabstudio.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
apt-transport-https \  
build-essential \  
libxslt1-dev \  
zlib1g-dev \  
python-imaging \  
python-numpy \  
python-dev \  
python-pip \  
sudo \  
git \  
wget \  
unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD bashrc /root/.bashrc  
ADD requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --additional-components app
kubectl alpha beta  
  
ENV PATH $PATH:/google-cloud-sdk/bin  
  
RUN gcloud components install app-engine-python  
RUN gcloud components update  
  
CMD ["bash"]  
  
EXPOSE 8000 8080  

