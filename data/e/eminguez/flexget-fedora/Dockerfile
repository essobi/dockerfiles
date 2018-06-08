FROM fedora:latest  
  
MAINTAINER Eduardo Minguez <edu@linux.com>  
  
RUN useradd flexget && \  
mkdir -p /home/flexget/flexget/{from,to} && \  
mkdir -p /home/flexget/.config/flexget && \  
chown -R flexget: /home/flexget/  
  
RUN dnf clean all && \  
dnf update -y && \  
dnf install -y python-pip python-virtualenv && \  
dnf clean all  
  
USER flexget  
WORKDIR /home/flexget  
  
RUN virtualenv ~/flexget/ && \  
cd ~/flexget/ && \  
bin/pip install flexget && \  
bin/pip install transmissionrpc  
  
VOLUME ["/home/flexget/flexget/from", "/home/flexget/flexget/to",
"/home/flexget/.config/flexget"]  
  
ADD files/run_flexget.sh /run_flexget.sh  
  
CMD ["/run_flexget.sh"]  

