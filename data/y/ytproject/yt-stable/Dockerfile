FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
  
#Runit  
RUN apt-get install -y runit  
CMD /usr/sbin/runsvdir-start  
  
#SSHD  
RUN apt-get install -y openssh-server && \  
mkdir -p /var/run/sshd  
RUN sed -i "s/session.*required.*pam_loginuid.so/#session required
pam_loginuid.so/" /etc/pam.d/sshd  
RUN sed -i "s/PermitRootLogin without-password/#PermitRootLogin without-
password/" /etc/ssh/sshd_config  
  
#Utilities  
RUN apt-get install -y vim less net-tools inetutils-ping \  
curl git telnet nmap socat dnsutils netcat tree htop \  
unzip sudo software-properties-common  
  
#Required by Python packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential \  
python-dev python-pip liblapack-dev libatlas-dev gfortran libfreetype6 \  
libfreetype6-dev libpng12-dev python-lxml libyaml-dev g++ libffi-dev \  
pkg-config  
  
#0MQ  
RUN cd /tmp && \  
wget http://download.zeromq.org/zeromq-4.0.4.tar.gz && \  
tar xvfz zeromq-4.0.4.tar.gz && \  
cd zeromq-4.0.4 && \  
./configure && \  
make install && \  
ldconfig  
  
#Upgrade pip  
RUN pip install -U setuptools  
RUN pip install -U pip  
  
#matplotlib needs latest distribute  
RUN pip install -U distribute  
  
RUN pip install numpy cython jinja2 pyzmq tornado  
  
#IPython  
RUN pip install ipython[notebook]  
ENV IPYTHONDIR /ipython  
RUN mkdir /ipython && \  
ipython profile create nbserver  
  
RUN pip install scipy sympy matplotlib  
  
# Mercurial  
RUN pip install mercurial python-hglib  
  
#Pattern  
RUN pip install --allow-external pattern  
  
#Install yt  
RUN cd /tmp && \  
hg clone -r stable http://bitbucket.org/yt_analysis/yt && \  
cd yt && \  
python2.7 setup.py install  
  
RUN apt-get install -y libhdf5-7 libhdf5-dev  
RUN pip install h5py  
  
#ThingKing  
RUN pip install requests thingking darksky_catalog  

