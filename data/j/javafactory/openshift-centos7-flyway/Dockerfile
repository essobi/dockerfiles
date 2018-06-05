FROM centos/s2i-base-centos7  
  
ENV APP_DIR /flyway  
ENV FLYWAY_VERSION 5.0.7  
WORKDIR ${APP_DIR}  
  
RUN INSTALL_PKGS="tar unzip bc which lsof java-1.8.0-openjdk
java-1.8.0-openjdk-devel" && \  
yum install -y --enablerepo=centosplus $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all -y  
  
RUN curl -L https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz -o
flyway-commandline-${FLYWAY_VERSION}.tar.gz \  
&& tar -xzf flyway-commandline-${FLYWAY_VERSION}.tar.gz --strip-components=1 \  
&& rm flyway-commandline-${FLYWAY_VERSION}.tar.gz \  
&& ln -s ${APP_DIR}/flyway /usr/local/bin/flyway  
  
### Setup user for build execution and application runtime  
#ENV APP_DIR=/opt/app-root  
#ENV PATH=${APP_DIR}/bin:${PATH} HOME=${APP_DIR}  
#COPY bin/ ${APP_DIR}/bin/  
RUN chmod +x ${APP_DIR}/flyway && \  
chgrp -R 0 ${APP_DIR} && \  
chmod +x /usr/local/bin/flyway  
  
#RUN chown -R 1001:0 /flyway/ && \  
# chown -R 1001:0 $HOME && \  
# chmod -R ug+rw /flyway/ && \  
# chmod -R u+rwx /flyway/flyway  
USER 1000070000  
WORKDIR ${APP_DIR}  
  
VOLUME ${APP_DIR}/sql  
  
CMD flyway  

