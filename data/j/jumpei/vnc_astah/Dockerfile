FROM hidetarou2013/centos6-vnc:JP_GUI  
MAINTAINER jumpei_oshiro<jumpei_oshiro@e-it.co.jp>  
  
#----------------------------  
# java8  
#----------------------------  
USER root  
ADD install_java8.sh /tmp/install_java8.sh  
RUN /bin/bash /tmp/install_java8.sh  
ENV JAVA_HOME /usr/java/latest  
ENV JRE_HOME /usr/java/latest  
  
#----------------------------  
# freemind  
#----------------------------  
#USER root  
RUN yum install -y unzip wget curl sudo  
RUN mkdir /tmp/astah  
WORKDIR /tmp/astah/  
ADD astah-community-7_0_0-846701.zip /tmp/astah/  
RUN unzip astah-community-7_0_0-846701.zip  
RUN mv /tmp/astah /usr/local/  
RUN ls -l /usr/local/astah  
RUN rm -f /usr/local/astah/astah-community-7_0_0-846701.zip  
RUN chmod 755 /usr/local/astah/astah_community/astah  
  
#----------------------------  
# tag:1280x1024  
#----------------------------  
WORKDIR /usr/bin  
RUN sed -i -e 's/1024x768/1280x1024/g' vncserver  
  
#----------------------------  
# run user:kioskuser  
#----------------------------  
USER kioskuser  
ENV LANG ja_JP.utf8  
RUN export LANG=ja_JP.UTF-8  
  
RUN /bin/echo "exec sh /usr/local/astah/astah_community/astah" >>
/home/kioskuser/.vnc/xstartup  
  
#EXPOSE 5901  
#ENTRYPOINT ["/usr/bin/vncserver","-fg"]  

