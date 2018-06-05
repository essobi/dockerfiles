FROM collokia/ubuntu-with-dev-utils  
  
EXPOSE 8085  
VOLUME "/bamboo/home"  
  
ENV BAMBOO_HOME=/bamboo/home \  
BAMBOO_VERSION=5.9.2 \  
ARTIFACTORY_PLUGIN_VERSION=1.8.0  
RUN mkdir -p /tmp/build /bamboo/installed "$BAMBOO_HOME" \  
&& wget https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz -O /tmp/build/bamboo.tgz && tar -xzf
/tmp/build/bamboo.tgz -C /bamboo/installed \  
&& ln -s /bamboo/installed/atlassian-bamboo-${BAMBOO_VERSION} /bamboo/current
\  
&& wget http://dl.bintray.com/jfrog/jfrog-jars/org/jfrog/bamboo/bamboo-
artifactory-plugin/${ARTIFACTORY_PLUGIN_VERSION}/bamboo-artifactory-
plugin-${ARTIFACTORY_PLUGIN_VERSION}.jar -O /bamboo/current/atlassian-
bamboo/WEB-INF/lib/bamboo-artifactory-plugin-${ARTIFACTORY_PLUGIN_VERSION}.jar
\  
&& rm -rf /var/tmp/build  
  
WORKDIR /bamboo/current  
ENTRYPOINT ["bash", "-ex", "/bamboo/current/bin/start-bamboo.sh", "-fg"]  

