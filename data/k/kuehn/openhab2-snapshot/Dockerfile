FROM kuehn/alpn-jdk8  
  
ARG OH_TARGET_URL=https://bintray.com/openhab/mvn  
ENV OPENHAB_HOME=/opt/openhab/ \  
OPENHAB_HTTP_PORT=8080 \  
TERM=xterm  
ARG OH_VER=2.0.0-SNAPSHOT  
RUN mkdir -p /opt/openhab/ \  
&& wget -qO openhab-download.zip
"https://openhab.ci.cloudbees.com/job/openHAB-
Distribution/lastSuccessfulBuild/artifact/distributions/openhab-
offline/target/openhab-offline-${OH_VER}.zip" \  
&& unzip openhab-download.zip -d /opt/openhab/ \  
&& rm -f openhab-download.zip  
ADD etc/supervisord.d/*.ini /etc/supervisord.d/  
ADD opt/openhab/configurations/ /opt/openhab/configurations/  
ADD opt/openhab/conf/ /opt/openhab/conf/  
ADD opt/qnib/openhab/bin/start.sh /opt/qnib/openhab/bin/start.sh  
  
CMD /opt/openhab/start.sh  

