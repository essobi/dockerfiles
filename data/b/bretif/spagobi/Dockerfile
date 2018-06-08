FROM java:7  
MAINTAINER bertrand@sudokeys.com  
  
ENV TOMCAT_VERSION 7.0.57  
ENV SPAGOBI_VERSION 5.1.0_19012015  
RUN mkdir -p /usr/share/tomcat  
RUN wget --no-verbose -O /tmp/apache-tomcat-$TOMCAT_VERSION.tar.gz \  
http://archive.apache.org/dist/tomcat/tomcat-7/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
# stop building if md5sum does not match  
RUN echo "d6a07b41203f876440c9a7c8581db153 /tmp/apache-
tomcat-$TOMCAT_VERSION.tar.gz" | \  
md5sum -c  
# install tomcat in /usr/share/tomcat  
RUN tar xzf /tmp/apache-tomcat-$TOMCAT_VERSION.tar.gz \  
\--strip-components=1 -C /usr/share/tomcat  
ENV CATALINA_HOME /usr/share/tomcat  
  
RUN apt-get install -y unzip wget  
  
RUN wget --no-verbose http://download.forge.ow2.org/spagobi/SpagoBI-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBI-bin-$SPAGOBI_VERSION.zip && \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBI-bin-$SPAGOBI_VERSION.zip &&
\  
rm -f /tmp/SpagoBI-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBIAccessibilityEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIAccessibilityEngine-
bin-$SPAGOBI_VERSION.zip && \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIAccessibilityEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIAccessibilityEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBIWhatIfEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIWhatIfEngine-bin-$SPAGOBI_VERSION.zip
&& \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIWhatIfEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIWhatIfEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBIBirtReportEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIBirtReportEngine-
bin-$SPAGOBI_VERSION.zip && \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIBirtReportEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIBirtReportEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBIChartEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIChartEngine-bin-$SPAGOBI_VERSION.zip
&& \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIChartEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIChartEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBICockpitEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBICockpitEngine-bin-$SPAGOBI_VERSION.zip
&& \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBICockpitEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBICockpitEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBICommonJEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBICommonJEngine-bin-$SPAGOBI_VERSION.zip
&& \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBICommonJEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBICommonJEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBIConsoleEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIConsoleEngine-bin-$SPAGOBI_VERSION.zip
&& \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIConsoleEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIConsoleEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBIDataMiningEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIDataMiningEngine-
bin-$SPAGOBI_VERSION.zip && \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIDataMiningEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIDataMiningEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose http://download.forge.ow2.org/spagobi/SpagoBIGeoEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIGeoEngine-bin-$SPAGOBI_VERSION.zip &&
\  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIGeoEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIGeoEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBIGeoReportEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIGeoReportEngine-
bin-$SPAGOBI_VERSION.zip && \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIGeoReportEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIGeoReportEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBIJasperReportEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIJasperReportEngine-
bin-$SPAGOBI_VERSION.zip && \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIJasperReportEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIJasperReportEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBIJPivotEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIJPivotEngine-bin-$SPAGOBI_VERSION.zip
&& \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIJPivotEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIJPivotEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBINetworkEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBINetworkEngine-bin-$SPAGOBI_VERSION.zip
&& \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBINetworkEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBINetworkEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose http://download.forge.ow2.org/spagobi/SpagoBIQbeEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBIQbeEngine-bin-$SPAGOBI_VERSION.zip &&
\  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBIQbeEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBIQbeEngine-bin-$SPAGOBI_VERSION.zip  
RUN wget --no-verbose
http://download.forge.ow2.org/spagobi/SpagoBITalendEngine-
bin-$SPAGOBI_VERSION.zip -O /tmp/SpagoBITalendEngine-bin-$SPAGOBI_VERSION.zip
&& \  
unzip -o -d /usr/share/tomcat/webapps /tmp/SpagoBITalendEngine-
bin-$SPAGOBI_VERSION.zip && \  
rm -f /tmp/SpagoBITalendEngine-bin-$SPAGOBI_VERSION.zip  
  
ADD ./resources/conf/server.xml /usr/share/tomcat/conf/server.xml  
  
ADD http://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc41.jar
/usr/share/tomcat/lib/postgresql-9.3-1102.jdbc41.jar  
  
ADD ./resources/install /root/install  
RUN chmod 755 /root/install && sync && /root/install  
  
#ADD ./resources/conf/SpagoBI/web.xml /usr/share/tomcat/webapps/SpagoBI/WEB-
INF/web.xml  
#ADD ./resources/conf/SpagoBIBirtReportEngine/web.xml
/usr/share/tomcat/webapps/SpagoBIBirtReportEngine/WEB-INF/web.xml  
#ADD ./resources/conf/SpagoBIConsoleEngine/web.xml
/usr/share/tomcat/webapps/SpagoBIConsoleEngine/WEB-INF/web.xml  
#ADD ./resources/SpagobiFilter.jar /usr/share/tomcat/lib/SpagobiFilter.jar  
CMD /usr/share/tomcat/bin/startup.sh && tail -F
/usr/share/tomcat/logs/catalina.out  
  
EXPOSE 8080  

