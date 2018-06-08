FROM alpine:3.7  
LABEL authors=suyunrong  
  
#=======================================  
# Set Coding  
#=======================================  
ENV LANG C.UTF-8  
  
#=======================================  
# Install base package  
#=======================================  
RUN apk upgrade -U \  
&& apk add \  
bash \  
wget \  
unzip \  
tzdata \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
#=======================================  
# Set timezone  
#=======================================  
ENV TZ "Asia/Shanghai"  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/TZ  
#=======================================  
# Install openjdk  
#=======================================  
RUN apk upgrade -U \  
&& apk add \  
openjdk8-jre \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
#=======================================  
# Config java_home  
#=======================================  
RUN echo "JAVA_HOME=\"/usr/lib/jvm/java-1.8-openjdk\"" >> /etc/profile \  
&& echo "export JAVA_HOME" >> /etc/profile \  
&& echo "export PATH=\"$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin\"" >>
/etc/profile  
#========================================  
# Tomcat config  
# http://mirrors.hust.edu.cn/apache/tomcat/tomcat-8/v8.0.51/bin/apache-
tomcat-8.0.51.tar.gz  
#========================================  
ENV VERSION "v8.5.31"  
ENV TOMCAT_VERSION "apache-tomcat-8.5.31"  
RUN wget \--no-verbose -O /tmp/$TOMCAT_VERSION.tar.gz
http://mirror.bit.edu.cn/apache/tomcat/tomcat-8/$VERSION/bin/$TOMCAT_VERSION.tar.gz
\  
&& mkdir -p /www/tomcat/ \  
&& tar -xzvf /tmp/$TOMCAT_VERSION.tar.gz -C /www/tomcat/ \  
&& mv /www/tomcat/$TOMCAT_VERSION /www/tomcat/pp-col-tomcat \  
&& tar -xzvf /tmp/$TOMCAT_VERSION.tar.gz -C /www/tomcat/ \  
&& mv /www/tomcat/$TOMCAT_VERSION /www/tomcat/pp-web-tomcat \  
&& rm -rf /www/tomcat/pp-col-tomcat/webapps/* \  
&& rm -rf /www/tomcat/pp-web-tomcat/webapps/* \  
&& sed -i 's/port="8005"/port="18005"/g' /www/tomcat/pp-col-
tomcat/conf/server.xml \  
&& sed -i 's/port="8080"/port="18080"/g' /www/tomcat/pp-col-
tomcat/conf/server.xml \  
&& sed -i 's/port="8443"/port="18443"/g' /www/tomcat/pp-col-
tomcat/conf/server.xml \  
&& sed -i 's/port="8009"/port="18009"/g' /www/tomcat/pp-col-
tomcat/conf/server.xml \  
&& sed -i 's/redirectPort="8443"/redirectPort="18443"/g' /www/tomcat/pp-col-
tomcat/conf/server.xml \  
&& sed -i 's/port="8005"/port="28005"/g' /www/tomcat/pp-web-
tomcat/conf/server.xml \  
&& sed -i 's/port="8080"/port="28080"/g' /www/tomcat/pp-web-
tomcat/conf/server.xml \  
&& sed -i 's/port="8443"/port="28443"/g' /www/tomcat/pp-web-
tomcat/conf/server.xml \  
&& sed -i 's/port="8009"/port="28009"/g' /www/tomcat/pp-web-
tomcat/conf/server.xml \  
&& sed -i 's/redirectPort="8443"/redirectPort="28443"/g' /www/tomcat/pp-web-
tomcat/conf/server.xml \  
&& rm -rf /tmp/$TOMCAT_VERSION.tar.gz  
  
#========================================  
# Hbase config  
# http://archive.apache.org/dist/hbase/1.2.6/hbase-1.2.6-bin.tar.gz  
#========================================  
COPY hbase-create.hbase /opt/bin/  
RUN wget \--no-verbose -O /tmp/hbase-1.2.6-bin.tar.gz
http://archive.apache.org/dist/hbase/1.2.6/hbase-1.2.6-bin.tar.gz \  
&& tar -xzvf /tmp/hbase-1.2.6-bin.tar.gz -C /www/ \  
&& mv /www/hbase-1.2.6 /www/hbase \  
&& mkdir -p /www/data \  
&& sed -i 's|# export JAVA_HOME=/usr/java/jdk1.6.0/|export
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk|g' /www/hbase/conf/hbase-env.sh \  
&& sed -i 's|</configuration>| <property>\r\n <name>hbase.rootdir</name>\r\n
<value>file:///data/hbase</value>\r\n </property>\r\n</configuration>|g'
/www/hbase/conf/hbase-site.xml \  
&& sed -i 's|export HBASE_MASTER_OPTS="$HBASE_MASTER_OPTS -XX:PermSize=128m
-XX:MaxPermSize=128m"|#export HBASE_MASTER_OPTS="$HBASE_MASTER_OPTS
-XX:PermSize=128m -XX:MaxPermSize=128m"|g' /www/hbase/conf/hbase-env.sh \  
&& sed -i 's|export HBASE_REGIONSERVER_OPTS="$HBASE_REGIONSERVER_OPTS
-XX:PermSize=128m -XX:MaxPermSize=128m"|#export
HBASE_REGIONSERVER_OPTS="$HBASE_REGIONSERVER_OPTS -XX:PermSize=128m
-XX:MaxPermSize=128m"|g' /www/hbase/conf/hbase-env.sh \  
&& rm -rf /tmp/hbase-1.2.6-bin.tar.gz \  
&& /www/hbase/bin/start-hbase.sh \  
&& sleep 5 \  
&& /www/hbase/bin/hbase shell /opt/bin/hbase-create.hbase  
#========================================  
# pinpoint config  
# https://github.com/naver/pinpoint/releases/download/1.7.3/pinpoint-
web-1.7.3.war  
# https://github.com/naver/pinpoint/releases/download/1.7.3/pinpoint-
collector-1.7.3.war  
#========================================  
RUN wget \--no-verbose -O /tmp/pinpoint-collector-1.7.3.war
https://github.com/naver/pinpoint/releases/download/1.7.3/pinpoint-
collector-1.7.3.war \  
&& wget \--no-verbose -O /tmp/pinpoint-web-1.7.3.war
https://github.com/naver/pinpoint/releases/download/1.7.3/pinpoint-
web-1.7.3.war \  
&& unzip /tmp/pinpoint-collector-1.7.3.war -d /www/tomcat/pp-col-
tomcat/webapps/ROOT \  
&& unzip /tmp/pinpoint-web-1.7.3.war -d /www/tomcat/pp-web-tomcat/webapps/ROOT
\  
&& rm -rf /tmp/pinpoint-collector-1.7.3.war \  
&& rm -rf /tmp/pinpoint-web-1.7.3.war  
#========================================  
# copy scripts  
#========================================  
COPY run.sh /opt/bin/  
#========================================  
# 开放端口组，ssh(22)，hbase(16010)，pp-col(18080)，pp-web(28080)  
#========================================  
EXPOSE 16010 18080 28080 9994 9995/udp 9996/udp  
  
# 运行脚本，启动sshd服务  
CMD ["/opt/bin/run.sh"]

