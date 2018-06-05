FROM arnaudeprez/java-agent-bond:8  
LABEL maintainer="Arnaud Deprez <arnaudeprez@gmail.com>"  
  
ENV H2_RELEASE_DATE=2017-06-10  
WORKDIR /tmp  
  
# Install H2  
RUN curl -sSL http://www.h2database.com/h2-$H2_RELEASE_DATE.zip -o
h2-$H2_RELEASE_DATE.zip && \  
unzip h2-$H2_RELEASE_DATE.zip && \  
rm -f h2-$H2_RELEASE_DATE.zip && \  
mv h2 /opt && \  
mkdir -p /opt/h2-data  
  
# Expose ports.  
# - 1521: H2 Server  
# - 80: H2 Console  
# - 8778: jolokia  
EXPOSE 1521 80 8778  
CMD java $(agent-bond-opts) -cp /opt/h2/bin/h2*.jar org.h2.tools.Server -web
-webAllowOthers -webPort 80 -tcp -tcpAllowOthers -tcpPort 1521 -baseDir
/opt/h2-data  

