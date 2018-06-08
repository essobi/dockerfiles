#Dockerfile for viosind daemon.  
from ubuntu:latest  
RUN \  
apt-get update && apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y curl vim wget  
RUN \  
apt-get install -y libc6-dev g++-multilib python pwgen  
RUN \  
wget https://github.com/davidTjr/Vision-
Project/releases/download/1.0.14/Vision_1.0.14_x64_Ubuntu16_04.tar.gz -o
vision.tar.gz  
RUN \  
mkdir /root/vision && mv /Vision_1.0.14_x64_Ubuntu16_04.tar.gz /root/vision/
&&\  
cd /root/vision && tar -xzf /root/vision/Vision_1.0.14_x64_Ubuntu16_04.tar.gz
&&\  
/root/vision/Vision_x64_Ubuntu16_04/fetch-params.sh && \  
rm /root/vision/Vision_1.0.14_x64_Ubuntu16_04.tar.gz  
COPY ./blocknotify.c /var/  
RUN cd /var && gcc blocknotify.c -o blocknotify && mv /var/blocknotify /bin &&
rm /var/blocknotify.c  
RUN \  
mkdir /root/.vision && touch /root/.vision/vision.conf &&\  
chmod +x /root/vision/Vision_x64_Ubuntu16_04/visiond  
RUN \  
echo "#!/bin/bash\n/root/vision/Vision_x64_Ubuntu16_04/visiond && bash" >
/root/entry.sh &&\  
chmod +x /root/entry.sh  
VOLUME ["/root/.vision"]  
ADD ./vision.conf /root/.vision/  
ENTRYPOINT ["/root/entry.sh"]  

