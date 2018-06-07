FROM ubuntu:trusty  
  
MAINTAINER Igor Bronovskyi <admin@brun.if.ua>  
  
# Install Java  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" >> /etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
RUN apt-get update  
RUN echo "oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN apt-get install oracle-java7-installer -y  
RUN apt-get install oracle-java7-set-default  
  
# echo JAVA_HOME="/usr/lib/jvm/java-7-oracle/" >> /etc/environment  
# Install GIT  
RUN apt-get install git -y  
  
# Install SSH  
RUN apt-get install -y openssh-server  
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN service ssh start  
RUN update-rc.d ssh defaults  
  
ADD ./gen-key.sh /root/gen-key.sh  
  
#CMD /root/gen-key.sh  
# Install davfs2  
RUN apt-get install davfs2 -y  
  
EXPOSE 22  
  
ADD ./start.sh /root/start.sh  
  
CMD /root/start.sh  
  

