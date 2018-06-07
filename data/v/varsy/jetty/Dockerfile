FROM centos:7  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
# java  
RUN yum update -y && yum install -y unzip  
  
ENV JAVA_VER=1.8.0_72 JAVA_DWL_VER=8u72 JAVA_DWL_BVER=b15  
ENV JAVA_HOME=/usr/java64/current JDK_HOME=${JAVA_HOME}  
ENV PATH ${JAVA_HOME}/bin:${PATH}  
  
RUN mkdir -p /usr/java64 ; cd /usr/java64/ ; \  
curl -L -o jdk-${JAVA_DWL_VER}-linux-x64.tar.gz --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/${JAVA_DWL_VER}-${JAVA_DWL_BVER}/jdk-${JAVA_DWL_VER}-linux-x64.tar.gz
&& \  
tar -xzf jdk-${JAVA_DWL_VER}-linux-x64.tar.gz && rm
jdk-${JAVA_DWL_VER}-linux-x64.tar.gz && \  
ln -s jdk${JAVA_VER} current && \  
chown -R root:root /usr/java64 && \  
chmod -R a+rwX /usr/java64  
  
# jetty  
ENV HOME=/home/jetty JETTY_VER=9.3.11.v20160721 TANUKI_VER=3.5.25  
RUN /usr/sbin/useradd jetty && cd /home/jetty && \  
curl -L -o /home/jetty/jetty.tar.gz
"http://eclipse.org/downloads/download.php?file=/jetty/$JETTY_VER/dist/jetty-
distribution-$JETTY_VER.tar.gz&r=1" && \  
tar zxf /home/jetty/jetty.tar.gz && mv jetty-distribution-$JETTY_VER jetty-
current && \  
curl -L -o /home/jetty/wrapper.tar.gz
"http://wrapper.tanukisoftware.com/download/$TANUKI_VER/wrapper-
linux-x86-64-$TANUKI_VER.tar.gz" && \  
tar zxf /home/jetty/wrapper.tar.gz && cp -rp wrapper-linux-*/*
/home/jetty/jetty-current/ && \  
rm -rf /home/jetty/wrapper.tar.gz /home/jetty/jetty.tar.gz
/home/jetty/wrapper-linux-x86-64-$TANUKI_VER  
  
RUN cp -p /home/jetty/jetty-current/src/bin/sh.script.in /home/jetty/jetty-
current/bin/jetty && \  
sed -i '/# Application/a export JAVA_HOME=\/usr\/java64\/current\nexport
JETTY_HOME=\/home\/jetty\/jetty-current\nexport JETTY_PORT=8081\n'
/home/jetty/jetty-current/bin/jetty && \  
sed -i "s/@app.name@/jetty/g" /home/jetty/jetty-current/bin/jetty && \  
sed -i "s/@app.long.name@/jetty/g" /home/jetty/jetty-current/bin/jetty && \  
sed -i "s/^WRAPPER_CMD=.*/WRAPPER_CMD=\"wrapper\"/" /home/jetty/jetty-
current/bin/jetty && \  
sed -i "s/^WRAPPER_CONF=.*/WRAPPER_CONF=\"\\.\\.\/conf\/wrapper.conf\"/"
/home/jetty/jetty-current/bin/jetty && \  
touch /home/jetty/jetty-current/conf/wrapper-additional.conf && \  
chmod +x /home/jetty/jetty-current/bin/jetty && \  
rm -f /home/jetty/jetty-current/webapps/test.war && rm -f /home/jetty/jetty-
current/contexts/*.xml && \  
chown -R jetty:jetty /home/jetty && \  
chmod -R a+rwX /home/jetty && \  
echo "STOP.PORT=8990" >> /home/jetty/jetty-current/start.ini && \  
echo "STOP.KEY=mysecretkey" >> /home/jetty/jetty-current/start.ini  
  
ADD run-jetty.sh /  
  
ADD wrapper.conf /home/jetty/jetty-current/conf/wrapper.conf  
  
CMD /run-jetty.sh  
  
EXPOSE 8081  

