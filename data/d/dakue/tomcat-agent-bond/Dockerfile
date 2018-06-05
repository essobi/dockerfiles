FROM tomcat:8-jre8  
MAINTAINER Daniel Kühne <dkhmailto@googlemail.com>  
  
ENV AB_VERSION="0.1.2" \  
AB_HOME="/opt/agent-bond"  
  
RUN set -x && \  
apt-get update && \  
apt-get install -y curl ca-certificates && \  
curl -sSL https://raw.githubusercontent.com/fabric8io/agent-bond/master/fish-
pepper/agent-bond/fp-files/agent-bond-opts -o /usr/local/bin/agent-bond-opts
&& \  
sed -i 's|/bin/sh|/bin/bash|g' /usr/local/bin/agent-bond-opts && \  
chmod 755 /usr/local/bin/agent-bond-opts && \  
mkdir -p $AB_HOME && \  
curl -sSL http://central.maven.org/maven2/io/fabric8/agent-bond-
agent/${AB_VERSION}/agent-bond-agent-${AB_VERSION}.jar -o $AB_HOME/agent-
bond.jar && \  
chmod 644 $AB_HOME/agent-bond.jar && \  
curl -sSL https://raw.githubusercontent.com/fabric8io/agent-bond/master/fish-
pepper/agent-bond/fp-files/jmx_exporter_config.json -o
$AB_HOME/jmx_exporter_config.json && \  
chmod 644 $AB_HOME/jmx_exporter_config.json && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
RUN set -x && \  
echo '' >> $CATALINA_HOME/bin/setenv.sh && \  
echo '# Agent Bond' >> $CATALINA_HOME/bin/setenv.sh && \  
echo 'JAVA_OPTS="$(agent-bond-opts) $JAVA_OPTS"' >>
$CATALINA_HOME/bin/setenv.sh  
  
EXPOSE 8778 9779  

