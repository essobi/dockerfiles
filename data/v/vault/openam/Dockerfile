FROM tomcat:8-jre8  
MAINTAINER Christoph Dwertmann <christoph.dwertmann@vaultsystems.com.au>  
RUN wget
https://github.com/OpenRock/OpenAM/releases/download/13.0.0/OpenAM-13.0.0.zip
&& \  
unzip *.zip && \  
mv *.war $CATALINA_HOME/webapps/openam.war && \  
rm *.zip  
ENV CATALINA_OPTS="-Xmx2048m -server"  
CMD perl -0pi.bak -e 's/<!--\n <Connector port="8443"/<Connector port="8443"
keystoreFile="\/opt\/server.keystore" keystorePass="$ENV{'KEYSTORE_PASS'}"/'
$CATALINA_HOME/conf/server.xml && \  
perl -0pi.bak -e 's/sslProtocol="TLS" \/>\n -->/sslProtocol="TLS" \/>/'
$CATALINA_HOME/conf/server.xml && \  
catalina.sh run  

