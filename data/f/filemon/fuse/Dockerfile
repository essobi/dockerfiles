# Ubuntu 13.10, Oracle JDK 7, FuseESB 6.0  
#  
# VERSION 0.0.1  
#  
FROM stackbrew/ubuntu:13.10  
MAINTAINER Jiri filemon Fabian "jiri.fabian@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOSTNAME fuse  
  
RUN apt-get update -q  
RUN apt-get upgrade -y -q  
RUN apt-get install -q -y wget ca-certificates software-properties-common  
RUN apt-get install unzip -y  
RUN apt-get install vim -y  
RUN apt-get install ssh -y  
RUN apt-get install sshpass -y  
  
# install Oracle JDK 7  
RUN apt-get install -q -y software-properties-common  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install oracle-java7-installer -y  
  
#FUSE ESB  
RUN mkdir -p /home/fuse  
RUN cd /home/fuse && wget --progress=bar:force
https://dl.dropboxusercontent.com/u/1154542/jboss-fuse-
full-6.0.0.redhat-024.zip  
RUN unzip /home/fuse/jboss-fuse-full-6.0.0.redhat-024.zip -d /home/fuse  
RUN mv /home/fuse/jboss-fuse-6.0.0.redhat-024 /home/fuse/fuse-6.0.0  
ADD system.properties /home/fuse/fuse-6.0.0/etc/  
ADD users.properties /home/fuse/fuse-6.0.0/etc/  
  
ADD fabric.karaf /home/fuse/fuse-6.0.0/  
ADD amq.karaf /home/fuse/fuse-6.0.0/  
  
RUN /home/fuse/fuse-6.0.0/bin/start && sleep 60s && sshpass -p admin ssh
-oStrictHostKeyChecking=no -t -p 8101 admin@localhost <
/home/fuse/fuse-6.0.0/fabric.karaf && /home/fuse/fuse-6.0.0/bin/stop  
RUN /home/fuse/fuse-6.0.0/bin/start && sleep 60s && sshpass -p admin ssh
-oStrictHostKeyChecking=no -t -p 8101 admin@localhost <
/home/fuse/fuse-6.0.0/amq.karaf && /home/fuse/fuse-6.0.0/bin/stop  
  
EXPOSE 8181 8101 61617 2181  
WORKDIR /home/fuse/fuse-6.0.0  
  
CMD /home/fuse/fuse-6.0.0/bin/start && tail -f
/home/fuse/fuse-6.0.0/data/log/fuse.log

