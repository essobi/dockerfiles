# install sumologic  
FROM ubuntu:14.04  
RUN apt-get -qq update  
RUN apt-get install -y wget  
RUN wget
https://www.dropbox.com/s/33ub66u3lxnvds9/sumocollector_19.119-6_amd64.deb  
RUN dpkg -i sumocollector_19.119-6_amd64.deb  
RUN rm sumocollector_19.119-6_amd64.deb  
ADD sumo.conf /etc/sumo.conf  
ADD source_file_docker.json /opt/source_file_docker.json  
ADD start_sumo /etc/my_init.d/start_sumo  
EXPOSE 5416/tcp  

