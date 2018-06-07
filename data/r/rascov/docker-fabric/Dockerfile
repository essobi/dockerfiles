FROM ubuntu:14.04  
MAINTAINER Charles Chan <rascov@gmail.com>  
  
ENV HOME /root  
  
WORKDIR $HOME  
RUN apt-get update && apt-get install -y sudo git tcpdump arping && \  
git clone https://github.com/mininet/mininet.git  
  
WORKDIR $HOME/mininet  
ADD multi_controller.patch .  
ADD kill.patch .  
RUN git checkout -b 2.2.1 2.2.1 && \  
git apply multi_controller.patch && \  
git apply kill.patch  
  
WORKDIR $HOME  
RUN ./mininet/util/install.sh -n3f && \  
apt-get clean && apt-get purge -y && apt-get autoremove -y && \  
rm -rf nbeesrc-feb-24-2015.zip netbee  
ADD fabric.py .  
  
CMD ["python", "fabric.py"]  

