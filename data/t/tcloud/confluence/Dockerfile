# tcloud/confluence  
# VERSION 0.1  
FROM tcloud/jdk:8  
MAINTAINER tcloud  
  
USER root  
  
ENV BASE_DIR /usr/local/confluence  
ENV VERSION 5.8.10  
ENV TARBALL_DIR atlassian-confluence-${VERSION}  
ENV TARBALL ${TARBALL_DIR}.tar.gz  
  
ADD install ${BASE_DIR}/install  
ADD https://downloads.atlassian.com/software/confluence/downloads/${TARBALL}
${BASE_DIR}/${TARBALL}  
  
RUN ls -lh ${BASE_DIR} && \  
tar xzf ${BASE_DIR}/${TARBALL} -C ${BASE_DIR} && \  
ln -s ${BASE_DIR}/${TARBALL_DIR} ${BASE_DIR}/current && \  
rm -f ${BASE_DIR}/${TARBALL}  
  
RUN mv ${BASE_DIR}/install/mysql-connector-java-5.1.31-bin.jar
${BASE_DIR}/current/confluence/WEB-INF/lib/ && \  
mv ${BASE_DIR}/current/confluence/WEB-INF/lib/atlassian-extras-
decoder-v2-3.2.jar ${BASE_DIR}/current/confluence/WEB-INF/lib/atlassian-
extras-decoder-v2-3.2.jar.bak && \  
mv ${BASE_DIR}/install/atlassian-extras-decoder-v2-3.1.1.jar
${BASE_DIR}/current/confluence/WEB-INF/lib/ && \  
mv ${BASE_DIR}/current/confluence/WEB-INF/atlassian-bundled-plugins/atlassian-
universal-plugin-manager-plugin-2.18.4.jar ${BASE_DIR}/current/confluence/WEB-
INF/atlassian-bundled-plugins/atlassian-universal-plugin-manager-
plugin-2.18.4.jar.bak && \  
mv ${BASE_DIR}/install/atlassian-universal-plugin-manager-plugin-2.15.jar
${BASE_DIR}/current/confluence/WEB-INF/atlassian-bundled-plugins/  
  
ENV CONFLUENCE_HOME ${BASE_DIR}/current  
ENV PATH $CONFLUENCE_HOME/bin:$PATH  
  
RUN echo "CONFLUENCE_HOME=$CONFLUENCE_HOME">> /etc/environment && \  
echo "PATH=\$CONFLUENCE_HOME/bin:$PATH">> /etc/environment  
  
EXPOSE 8090  
WORKDIR /usr/local/confluence/current  
  
VOLUME ["/usr/local/confluence/current","/var/atlassian/application-
data/confluence","/var/lib/confluence","/data","/log"]  
  
# We use the "sh -c" to turn around
https://github.com/docker/docker/issues/5509 - variable not expanded  
ENTRYPOINT ["sh", "-c"]  
  
CMD ["/usr/local/confluence/current/bin/start-confluence.sh -fg"]

