# DESCRIPTION Pinpoint APM Web (User Interface)  
# TO_BUILD docker build -t pinpoint-web .  
# TO_RUN docker run -d -p 8080:8080 --net=host -e HBASE_HOST=<HOST_IP> -e
HBASE_PORT=2181 --name=pinpoint-web pinpoint-web  
  
FROM tomcat:8-jre8  
  
ENV PINPOINT_VERSION=1.6.2  
  
ADD start-web.sh /usr/local/bin/  
ADD mail.zip /assets/mail.zip  
  
RUN chmod a+x /usr/local/bin/start-web.sh \  
&& mkdir -p /assets/ \  
&& curl -SL
https://raw.githubusercontent.com/naver/pinpoint/$PINPOINT_VERSION/web/src/main/resources/pinpoint-
web.properties -o /assets/pinpoint-web.properties \  
&& curl -SL
https://raw.githubusercontent.com/naver/pinpoint/$PINPOINT_VERSION/web/src/main/resources/hbase.properties
-o /assets/hbase.properties \  
&& curl -SL
https://github.com/naver/pinpoint/releases/download/$PINPOINT_VERSION/pinpoint-
web-$PINPOINT_VERSION.war -o pinpoint-web.war \  
&& curl -SL
https://maven.java.net/content/repositories/releases/com/sun/mail/javax.mail/1.5.2/javax.mail-1.5.2.jar
-o javax.mail-1.5.2.jar \  
&& rm -rf /usr/local/tomcat/webapps \  
&& mkdir -p /usr/local/tomcat/webapps \  
&& unzip pinpoint-web.war -d /usr/local/tomcat/webapps/ROOT \  
&& rm -rf pinpoint-web.war \  
&& mv javax.mail-1.5.2.jar /usr/local/tomcat/webapps/ROOT/WEB-INF/lib/ \  
&& unzip /assets/mail.zip -d /usr/local/tomcat/webapps/ROOT/WEB-INF/classes/ \  
&& rm -rf /assets/mail.zip  
  
EXPOSE 8080  
  
ENTRYPOINT ["/usr/local/bin/start-web.sh"]

