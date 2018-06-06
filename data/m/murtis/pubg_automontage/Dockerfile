FROM ubuntu:16.04  
MAINTAINER Curtis Muntz <cmuntz@outlook.com>  
  
# update ubuntu  
RUN apt-get update && \  
apt-get upgrade -y --no-install-recommends && \  
apt-get install software-properties-common -y  
RUN add-apt-repository ppa:jonathonf/ffmpeg-3 && \  
apt-get update && \  
apt-get install -y \  
ffmpeg \  
libav-tools \  
x264 \  
x265 \  
python3 \  
python3-pip \  
python3-virtualenv \  
python3-setuptools \  
vim \  
\--no-install-recommends  
  
RUN mkdir /usr/src/app  
COPY requirements.txt /usr/src/app/requirements.txt  
RUN pip3 install -r /usr/src/app/requirements.txt  
  
# cleanup from all the apt stuff...  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/io  
COPY ./pubg_automontage/pubg_automontage.py /usr/src/app  
RUN chmod +x /usr/src/app/pubg_automontage.py  
CMD /usr/src/app/pubg_automontage.py  

