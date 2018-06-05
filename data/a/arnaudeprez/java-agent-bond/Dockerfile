FROM openjdk:7-alpine  
MAINTAINER Arnaud Deprez <arnaudeprez@gmail.com>  
  
#Install Agent Bond  
ENV AB_VERSION=1.0.2 \  
AB_HOME="/opt/agent-bond"  
  
RUN set -x && \  
apk add --no-cache curl && \  
mkdir -p $AB_HOME && \  
curl -sSL https://raw.githubusercontent.com/fabric8io/agent-bond/master/fish-
pepper/agent-bond/fp-files/agent-bond-opts -o /usr/local/bin/agent-bond-opts
&& \  
chmod 755 /usr/local/bin/agent-bond-opts && \  
curl -sSL http://central.maven.org/maven2/io/fabric8/agent-bond-
agent/${AB_VERSION}/agent-bond-agent-${AB_VERSION}.jar -o $AB_HOME/agent-
bond.jar && \  
chmod 444 $AB_HOME/agent-bond.jar && \  
curl -sSL https://raw.githubusercontent.com/fabric8io/agent-bond/master/fish-
pepper/agent-bond/fp-files/jmx_exporter_config.json -o
$AB_HOME/jmx_exporter_config.json && \  
chmod 444 $AB_HOME/jmx_exporter_config.json  
  
# Print out the version  
CMD ["java", "-jar", "/opt/agent-bond/agent-bond.jar", "--version"]  

