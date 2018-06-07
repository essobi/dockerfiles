FROM centos:centos6  
MAINTAINER Jouni Rajala  
RUN yum update -y  
RUN yum install -y openssh-server supervisor unzip wget patch gcc-c++ python-
setuptools  
RUN easy_install supervisor  
  
RUN useradd unityserver  
RUN mkdir -p /home/unityserver/Production/MasterServer  
  
RUN wget http://unity3d.com/files/master-server/Facilitator-2.0.1f1.zip -O
/home/unityserver/Facilitator.zip  
RUN unzip /home/unityserver/Facilitator.zip -d
/home/unityserver/Production/Facilitator/  
RUN chown unityserver.unityserver -R /home/unityserver  
  
RUN cd /home/unityserver/Production/Facilitator/ && make  
  
EXPOSE 50005/udp 50005/tcp  
USER unityserver  
WORKDIR /home/unityserver/Production/Facilitator  
ENTRYPOINT exec /home/unityserver/Production/Facilitator/Facilitator  

