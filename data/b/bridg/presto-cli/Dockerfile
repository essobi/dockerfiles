FROM bridg/java  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV PRESTO_VERSION=0.144 \  
PRESTO_CLI_HOME=/opt/presto-cli \  
PRESTO_CLI_JAR=/opt/presto-cli/presto-cli-${PRESTO_VERSION}-executable.jar  
  
# Install PrestoDB  
RUN mkdir -p "/opt/presto-cli" \  
&& wget "https://repo1.maven.org/maven2/com/facebook/presto/presto-
cli/${PRESTO_VERSION}/presto-cli-${PRESTO_VERSION}-executable.jar" \  
-q -O "$PRESTO_CLI_JAR" \  
&& chmod +x "$PRESTO_CLI_JAR" \  
&& ln -s "$PRESTO_CLI_JAR" /usr/local/bin/presto \  
&& apt-get update \  
&& apt-get -y install less \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["presto"]  

