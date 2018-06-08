# Loaders  
# Image Loader  
# Markup Loader  
# References:  
#
http://docs.opencv.org/3.0-beta/doc/tutorials/introduction/desktop_java/java_dev_intro.html  
# http://rodrigoberriel.com/2014/10/installing-opencv-3-0-0-on-ubuntu-14-04/  
FROM sbubmi/pathomics_featuredb  
MAINTAINER Ganesh Iyer "lastlegion@gmail.com"  
ENV OPENCV_JAVA_DIR=/usr/local/share/OpenCV/java  
ENV OPENCV_JAVA_LIB=$OPENCV_JAVA_DIR/opencv-310.jar  
  
WORKDIR /root  
#RUN yum -y install nodejs  
RUN git clone https://github.com/camicroscope/uAIMDataLoader.git
annotationloader  
  
WORKDIR /root/annotationloader  
  
RUN npm install  
  
RUN npm install yargs #Annoying unlisted kue dependency  
COPY config.js.annotationsloader config.js  
  
WORKDIR /root  
  
# RUN apt-get -q update  
# RUN apt-get -q -y upgrade  
RUN "sh" "-c" "echo nameserver 8.8.8.8 >> /etc/resolv.conf"  
  
RUN yum -y install redis  
  
# Install forever  
#RUN ln -s "$(which nodejs)" /usr/bin/node  
RUN npm install -g forever  
  
# Install new zip loader  
COPY redis.conf /etc/redis/redis.conf  
  
WORKDIR /root  
COPY run.sh /root/  
#RUN yum -y install initscripts  
RUN yum -y install initscripts && yum clean all  
COPY trusted-app-client-0.0.1-jar-with-dependencies.jar /root/  
COPY createUser.py /root/  
  
CMD ["sh", "run.sh"]  

