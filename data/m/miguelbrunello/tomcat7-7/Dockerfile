FROM miguelbrunello/base  
  
#MAINTAINER Maluuba Infrastructure Team <infrastructure@maluuba.com>  
MAINTAINER Miguel Brunello <miguel.brunello@unc.edu.ar>  
EXPOSE 8080  
RUN apt-get -qq update && apt-get install -y \  
openjdk-7-jre \  
tomcat7 \  
curl  
  
#RUN rm -rf /var/lib/apt/lists/*  
#RUN sed -i 's/^\\(\\[supervisord\\]\\)$/\1\nnodaemon=true/'
/etc/supervisor/supervisord.conf  
RUN mv /etc/cron.daily/logrotate /etc/cron.hourly/logrotate  
ADD logrotate /etc/logrotate.d/tomcat7  
RUN chmod 644 /etc/logrotate.d/tomcat7  
ADD catalina.conf /etc/supervisord.d/catalina.conf  
ENV CATALINA_HOME /var/lib/tomcat7  
ENV PATH $CATALINA_HOME/bin:$PATH  
ADD data/sample.war $CATALINA_HOME/webapps/sample.war  
  
ENV CATALINA_OLD /usr/share/tomcat7  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
RUN ln -s $CATALINA_OLD/bin/ $CATALINA_HOME/bin  
RUN ln -s $CATALINA_OLD/lib/ $CATALINA_HOME/lib  
RUN mkdir -p $CATALINA_HOME/temp  
  
ENTRYPOINT ["/start.sh"]  

