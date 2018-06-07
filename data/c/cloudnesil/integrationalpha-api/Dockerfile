FROM cloudnesil/jetty-8-jre  
  
ENV RELIC_LOCATION /newrelic  
ENV WAR_LOCATION /opt/warfile  
ENV WEAVER_LOCATION /opt/weaverfile  
ENV JAVA_OPTIONS -javaagent:$WEAVER_LOCATION/aspectjweaver.jar
-javaagent:$RELIC_LOCATION/newrelic.jar  
ENV JETTY_BASE /var/lib/jetty  
ENV JETTY_HOME /usr/local/jetty  
ENV PATH $JETTY_HOME/bin:$PATH  
RUN mkdir -p "$WAR_LOCATION"  
RUN mkdir -p "$WEAVER_LOCATION"  
RUN mkdir -p "$RELIC_LOCATION"  
  
WORKDIR $WAR_LOCATION  
RUN wget -O integrationalpha.war https://s3-eu-
west-1.amazonaws.com/integrationalphaproject/integrationalpha.war  
ADD aspectjweaver.jar $WEAVER_LOCATION/  
ADD newrelic.jar $RELIC_LOCATION/  
ADD newrelic.yml $RELIC_LOCATION/  
  
WORKDIR $JETTY_BASE/webapps  
RUN wget https://s3-eu-
west-1.amazonaws.com/integrationalphaproject/integrationalpha.xml  
  
## Currently we need to tweak nsswitch.conf(5), mainly due to zettio/weave#68  
RUN sed 's/^\\(hosts:[\ ]*\\)\\(files\\)\ \\(dns\\)$/\1\3 \2/' -i
/etc/nsswitch.conf  
  
VOLUME $JETTY_BASE  
VOLUME $WAR_LOCATION  
VOLUME $JETTY_HOME  
VOLUME $WEAVER_LOCATION  
  
EXPOSE 8080  
EXPOSE 7171  
ENV TAKIPI_LOCATION /opt/takipi  
RUN mkdir -p "$TAKIPI_LOCATION"  
WORKDIR /tmp  
  
# Installing Takipi via apt-get and setting up key  
RUN echo "deb [arch=amd64] http://takipi-deb-repo.s3.amazonaws.com stable
main" > /etc/apt/sources.list.d/takipi.list  
ENV DEBIAN_FRONTEND noninteractive  
RUN wget -O - http://takipi-deb-repo.s3.amazonaws.com/hello@takipi.com.gpg.key
| apt-key add -  
RUN apt-get update  
RUN apt-get install takipi  
  
# Overriding binaries with the Heroku version of Takipi  
RUN wget https://s3.amazonaws.com/app-takipi-com/deploy/linux/takipi-latest-
heroku.tar.gz -O takipi-heroku.tar.gz  
RUN tar zxvf takipi-heroku.tar.gz  
RUN mv .takipi takipi  
RUN cp -r takipi /opt  
  
ENV PATH $PATH:$TAKIPI_LOCATION/bin  
ENV TAKIPI_SERVICE_PARAMS --xmx=180M  
  
RUN $TAKIPI_LOCATION/etc/takipi-setup-secret-key
S11400#ZQGFzoQ23rlpOI8P#wVgW21C5NdBPLrNt9cocVhCzHewJXy/bT4KPBVojcHI=#0116  
  
# Set server name  
RUN $TAKIPI_LOCATION/etc/takipi-setup-machine-name Nesil-Takipi  
  
CMD ["jetty.sh", "run"]

