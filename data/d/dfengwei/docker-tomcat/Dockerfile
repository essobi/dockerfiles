FROM openjdk:8-jre  
  
MAINTAINER dfengwei@163.com  
  
ENV JAVA_HOME /docker-java-home  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
ENV TIME_ZONE Asia/Shanghai  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
RUN set -x \  
\  
# 下载Tomcat压缩文件  
&& wget -O tomcat.tar.gz
'https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-8/v8.5.30/bin/apache-
tomcat-8.5.30.tar.gz' \  
# 解压  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
# 删除供Windows系统使用的.bat文件  
&& rm bin/*.bat \  
# 删除Tomcat压缩文件  
&& rm tomcat.tar.gz* \  
\  
# 更改时区  
&& echo "${TIME_ZONE}" > /etc/timezone \  
&& ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \  
\  
# 处理tomcat启动慢问题（随机数产生器初始化过慢）  
&& sed -i
"s#securerandom.source=file:/dev/random#securerandom.source=file:/dev/./urandom#g"
$JAVA_HOME/jre/lib/security/java.security \  
\  
# 启用gzip压缩  
&& sed -i 's/\\(<Connector port="8080" protocol="HTTP\/1.1"\\)/\1
compression="on" /' conf/server.xml  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

