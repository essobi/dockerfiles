FROM ubuntu:14.04  
MAINTAINER Aashish Chaudhary <aashish.chaudhary@kitware.com>  
  
EXPOSE 8001  
# bower does't work particularly well as root, so we create a non-root user  
# called kwuser, but give it sudo ability.  
RUN adduser --disabled-password --gecos '' kwuser && \  
adduser kwuser sudo && \  
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
RUN apt-get update && apt-get install -y curl \  
software-properties-common \  
python-software-properties \  
build-essential \  
libffi-dev \  
libpython-dev \  
python-bcrypt \  
python-pip \  
git \  
nodejs \  
npm  
  
RUN ln -s `which nodejs` /usr/bin/node  
  
RUN npm install -g bower  
  
USER root  
COPY etc/girder.cfg /etc/girder.cfg  
  
USER kwuser  
WORKDIR /home/kwuser  
  
RUN git clone \--depth 1 https://github.com/memex-explorer/memex-terra.git  
WORKDIR /home/kwuser/memex-terra  
  
RUN sudo pip install -r requirements.txt  
  
WORKDIR /home/kwuser/memex-terra/src  
RUN bower update  
  
CMD ["python", "main.py"]  

