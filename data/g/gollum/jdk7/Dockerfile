# version: 0.0.1  
FROM centos:latest  
  
MAINTAINER Gollum 'jianqiao.ms@foxmail.com'  
ENV PKG jdk-7u80-linux-x64.tar.gz  
ENV DIR jdk1.7.0_80  
ENV DST /usr/local/java  
ENV PROFILE /etc/profile.d/java.sh  
  
RUN yum install -y wget  
RUN wget https://packages.jianqiao.tk/$PKG && tar zxvf $PKG && \  
mv $DIR /opt/ && ln -s /opt/$DIR $DST && \  
echo "JAVA_HOME=$DST" > $PROFILE && \  
echo 'CLASSPATH=$JAVA_HOME/lib' >> $PROFILE && \  
echo 'pathmunge $JAVA_HOME/bin' >> $PROFILE && \  
rm -rf $PKG $DIR  
  
CMD ["/bin/bash"]  

