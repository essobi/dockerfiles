FROM anapsix/alpine-java:8  
# Configuration variables  
ENV BITBUCKET_HOME /var/atlassian/bitbucket  
ENV BITBUCKET_INSTALL /opt/atlassian/bitbucket  
ENV BITBUCKET_VERSION 5.9.0  
# Install Atlassian BitBucket and helper tools  
RUN apk --update add curl tar git perl \  
&& mkdir -p ${BITBUCKET_HOME} \  
&& mkdir -p ${BITBUCKET_INSTALL} \  
&& curl -Ls
"https://www.atlassian.com/software/stash/downloads/binary/atlassian-
bitbucket-${BITBUCKET_VERSION}.tar.gz" | tar -xz --directory
"${BITBUCKET_INSTALL}" \--strip-components=1 --no-same-owner \  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.36.tar.gz" | tar -xz --directory "${BITBUCKET_INSTALL}/lib" \--strip-
components=1 --no-same-owner "mysql-connector-java-5.1.36/mysql-connector-
java-5.1.36-bin.jar" \  
&& chown -R daemon:daemon ${BITBUCKET_INSTALL} \  
&& chown -R daemon:daemon ${BITBUCKET_HOME}  
  
EXPOSE 7990  
EXPOSE 7999  
USER daemon:daemon  
  
VOLUME ${BITBUCKET_HOME}  
  
WORKDIR ${BITBUCKET_HOME}  
  
CMD ["sh", "-c", "${BITBUCKET_INSTALL}/bin/start-bitbucket.sh -fg"]  

