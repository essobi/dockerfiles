FROM sergeyzh/centos6-java:jdk8  
MAINTAINER Andrey Sizov, andrey.sizov@jetbrains.com  
  
RUN /usr/sbin/useradd jetty  
  
ENV HOME=/home/jetty JETTY_VER=9.3.11.v20160721 TANUKI_VER=3.5.25  
  
RUN cd /home/jetty && \  
wget -O /home/jetty/jetty.tar.gz
"http://eclipse.org/downloads/download.php?file=/jetty/$JETTY_VER/dist/jetty-
distribution-$JETTY_VER.tar.gz&r=1" && \  
tar zxf /home/jetty/jetty.tar.gz && mv jetty-distribution-$JETTY_VER jetty-
current && \  
wget -O /home/jetty/wrapper.tar.gz
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
ln -s /home/jetty/jetty-current/bin/jetty /etc/init.d/ && chmod +x
/etc/init.d/jetty && \  
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

