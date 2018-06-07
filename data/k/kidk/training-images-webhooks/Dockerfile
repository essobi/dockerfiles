FROM ubuntu:16.04  
MAINTAINER Frederick Ryckbosch <fred@coscale.com>  
  
ENV PYTHONUNBUFFERED 0  
  
ENV FTP_URL ftp://debug-store/  
  
RUN apt-get update && apt-get install -y curl apt-transport-https python3
python3-pip && \  
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \-
&& \  
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" >
/etc/apt/sources.list.d/kubernetes.list && \  
apt-get update && apt-get install -y kubectl && \  
pip3 install Flask==0.12.2 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY webhooks.py /opt/webhooks/webhooks.py  
  
WORKDIR /opt/webhooks  
CMD [ "python3", "webhooks.py" ]  

