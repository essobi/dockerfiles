FROM tomcat:8.0-jre8-alpine  
  
ENV TIMEZONE="America/New_York"  
ENV XMS=2g XMX=4g
BANNERDB_JDBC=jdbc:oracle:thin:@//oracle.example.edu:1521/prod \  
BANPROXY_USERNAME=banproxy \  
BANPROXY_INITALSIZE=25 \  
BANPROXY_MAXTOTAL=400 \  
BANPROXY_MAXIDLE=-1 \  
BANPROXY_MAXWAIT=30000 \  
BANSSUSER_USERNAME=ban_ss_user \  
BANSSUSER_INITALSIZE=25 \  
BANSSUSER_MAXTOTAL=400 \  
BANSSUSER_MAXIDLE=-1 \  
BANSSUSER_MAXWAIT=30000  
ENV CATALINA_OPTS="-server -Xms\$XMS -Xmx\$XMX -Duser.timezone=\$TIMEZONE"  
RUN apk add --no-cache xmlstarlet \  
&& rm -Rf /usr/local/tomcat/webapps/* \  
&& apk add --no-cache tzdata \  
&& cp /usr/share/zoneinfo/$TIMEZONE /etc/localtime \  
&& addgroup -S tomcat \  
&& adduser -S -G tomcat -h /usr/local/tomcat tomcat  
  
ADD
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/ojdbc7/12.1.0.2/ojdbc7-12.1.0.2.jar
/usr/local/tomcat/lib/ojdbc7.jar  
ADD
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/xdb6/12.1.0.2/xdb6-12.1.0.2.jar
/usr/local/tomcat/lib/xdb6.jar  
  
RUN cd /usr/local/tomcat/lib/ \  
&& apk add --no-cache curl \  
&& curl
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/ojdbc7/12.1.0.2/ojdbc7-12.1.0.2.jar.sha1
--output ojdbc7.jar.sha1 \  
&& echo -n " ojdbc7.jar" >> ojdbc7.jar.sha1 \  
&& sha1sum -c ojdbc7.jar.sha1 \  
&& curl
https://developer.byu.edu/maven2/content/groups/thirdparty/com/oracle/xdb6/12.1.0.2/xdb6-12.1.0.2.jar.sha1
--output xdb6.jar.sha1 \  
&& echo -n " xdb6.jar" >> xdb6.jar.sha1 \  
&& sha1sum -c xdb6.jar.sha1 \  
&& rm *.sha1 \  
&& chown tomcat:tomcat ojdbc7.jar xdb6.jar && chmod +r ojdbc7.jar xdb6.jar  
  
COPY context.xml /usr/local/tomcat/conf/context.xml  
COPY server.xml /usr/local/tomcat/conf/server.xml  
COPY run.sh /usr/local/tomcat/bin  
  
# Configure logging to forward tomcat logs to docker log collector  
COPY logging.properties /usr/local/tomcat/conf/logging.properties  
RUN ln -s /dev/stderr /usr/local/tomcat/logs/localhost.log  
RUN ln -s /dev/stderr /usr/local/tomcat/logs/stacktrace.log  
  
RUN mkdir -p /opt/banner/config && mkdir -p /opt/banner/images && chown -R
tomcat:tomcat /opt/banner  
  
RUN chown -R tomcat:tomcat /usr/local/tomcat && chmod +x
/usr/local/tomcat/bin/run.sh  
  
EXPOSE 8080  
USER tomcat  
CMD ["bin/run.sh"]  

