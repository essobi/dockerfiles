FROM centos:centos6  
MAINTAINER Jouni Rajala  
RUN yum update -y  
RUN yum install -y openssh-server supervisor unzip wget patch gcc-c++ python-
setuptools  
RUN easy_install supervisor  
  
RUN useradd unityserver  
RUN mkdir -p /home/unityserver/Production/MasterServer  
  
RUN wget http://unity3d.com/files/master-server/MasterServer-2.0.1f1.zip -O
/home/unityserver/MasterServer.zip  
RUN unzip /home/unityserver/MasterServer.zip -d
/home/unityserver/Production/MasterServer/  
RUN chown unityserver.unityserver -R /home/unityserver  
  
RUN cd /home/unityserver/Production/MasterServer/ && make  
  
EXPOSE 23466/tcp 23466/udp  
USER unityserver  
WORKDIR /home/unityserver/Production/MasterServer  
ENTRYPOINT exec /home/unityserver/Production/MasterServer/MasterServer -s 3600  

