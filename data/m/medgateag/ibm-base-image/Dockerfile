From ubuntu:16.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get update -y && apt-get install --fix-missing -y \  
unzip \  
git \  
vim \  
sudo \  
nginx \  
supervisor \  
python3 \  
virtualenv \  
python3-pip \  
uwsgi-plugin-python \  
libgfortran3 \  
gfortran \  
nmon \  
language-pack-en \  
cron  
  
RUN locale-gen en_US.UTF-8  
  
RUN pip3 install --upgrade pip  
  
RUN ["/bin/bash", "-c", "cd /etc/ && virtualenv --python=/usr/bin/python3
--system-site-packages aite-api-env && source /etc/aite-api-env/bin/activate
&& pip install uwsgi && deactivate"]  
  
COPY ibm-base-image.version /home/aida/  
  
COPY requirements.txt /tmp  
RUN pip3 install numpy==1.13.3  
RUN pip3 install -r /tmp/requirements.txt  
  
# nginx config  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  

