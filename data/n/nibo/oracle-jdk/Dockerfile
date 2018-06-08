FROM nibo/centos:7.3.1611  
MAINTAINER Richard <nibocn@gmail.com>  
  
ENV TZ=Asia/Shanghai  
  
RUN cd /tmp \  
&& mkdir -p /opt/java \  
&& curl -o jdk-8u112-linux-x64.tar.gz -L -O -H "Cookie: oraclelicense=accept-
securebackup-cookie" -k
"http://ftp.wsisiz.edu.pl/pub/pc/pozyteczne%20oprogramowanie/java/8u112/jdk-8u112-linux-x64.tar.gz"
\  
&& tar xf jdk-8u112-linux-x64.tar.gz -C /opt/java \  
&& rm -rf jdk-8u112-linux-x64.tar.gz \  
&& ln -s /opt/java/jdk* /opt/java/jdk \  
&& ln -s /opt/java/jdk /opt/java/jvm \  
&& ln -s /opt/java/jdk/bin/java /usr/local/bin \  
&& ln -s /opt/java/jdk/bin/javac /usr/local/bin \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/timezone  
  
ENV JAVA_HOME /opt/java/jdk  
ENV PATH $JAVA_HOME/bin:$PATH  

