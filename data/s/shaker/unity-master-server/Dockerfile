FROM centos:centos6  
MAINTAINER Shaker Qawasmi - "http://github.com/sqawasmi"  
RUN yum update -y  
RUN yum install -y openssh-server supervisor unzip wget patch gcc-c++ python-
setuptools  
RUN easy_install supervisor  
  
RUN useradd unityserver  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /home/unityserver/Production/MasterServer  
  
RUN wget http://unity3d.com/files/master-server/MasterServer-2.0.1f1.zip -O
/home/unityserver/MasterServer.zip  
RUN unzip /home/unityserver/MasterServer.zip -d
/home/unityserver/Production/MasterServer/  
RUN chown unityserver.unityserver -R /home/unityserver  
ADD ./files/RakNet001.patch /home/unityserver/Production/MasterServer/  
RUN cd /home/unityserver/Production/MasterServer/ && patch -p0 -i
RakNet001.patch  
  
RUN cd /home/unityserver/Production/MasterServer/ && make  
  
RUN echo 'root:unityserver' |chpasswd  
  
ADD ./files/supervisord.conf /usr/supervisord.conf  
  
EXPOSE 22 23466  
CMD ["/usr/bin/supervisord"]  

