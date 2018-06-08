FROM openjdk:8-jdk-alpine  
  
MAINTAINER Brad Pinter "brad.pinter@gmail.com"  
# This is the release of swagger-codegen to pull in.  
LABEL vendor="Swagger" \  
io.swagger.swagger-codegen.version="2.2.0" \  
io.swagger.swagger-codegen.release-date="2016-07-17"  
  
ENV PUID 1000  
ENV PGID 1000  
ENV DEBUG 0  
ENV MVN_VERSION 3.3.9  
ENV SWAGGER_CODEGEN_TAG 2.2.0  
ENV SWAGGER_CODEGEN_GIT_REPO http://github.com/swagger-api/swagger-codegen.git  
  
# create dev user  
RUN apk --update add --no-cache bash sudo wget git ca-certificates && \  
addgroup -g $PGID dev && \  
adduser -h /config -u $PUID -H -D -G dev -s /bin/bash dev && \  
sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \  
sed -ri 's/# %wheel ALL=\\(ALL\\) NOPASSWD: ALL/%wheel ALL=\\(ALL\\) NOPASSWD:
ALL/' /etc/sudoers  
  
# Install Maven  
RUN wget \  
http://apache.mirrors.tds.net/maven/maven-3/3.3.9/binaries/apache-
maven-${MVN_VERSION}-bin.tar.gz && \  
tar -zxvf apache-maven-${MVN_VERSION}-bin.tar.gz && \  
rm apache-maven-${MVN_VERSION}-bin.tar.gz && \  
mv apache-maven-${MVN_VERSION} /usr/lib/mvn  
  
# Download swagger-codegen  
RUN mkdir -p /opt && \  
git clone \--branch v$SWAGGER_CODEGEN_TAG \--depth 1 $SWAGGER_CODEGEN_GIT_REPO
\  
/opt/swagger-codegen  
  
# Build swagger-codegen  
WORKDIR /opt/swagger-codegen  
RUN /usr/lib/mvn/bin/mvn clean package && \  
mv /opt/swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-
cli.jar /opt/ && \  
mv /opt/swagger-codegen/modules/swagger-codegen/target/swagger-
codegen-2.2.0.jar /opt/ && \  
mv /opt/swagger-codegen/modules/swagger-generator/target/swagger-
generator-2.2.0.war /opt/  
WORKDIR /opt  
RUN rm -rf /opt/swagger-codegen/  
  
RUN apk del --purge wget ca-certificates git && \  
rm -rf /var/cache/apk/*  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will  
# belong to root.  
RUN mkdir /data /output /state /config  
RUN touch /data/.extra /output/.extra /state/.extra /config/.extra  
RUN chown -R dev:dev /data && \  
chown -R dev:dev /output && \  
chown -R dev:dev /state && \  
chown -R dev:dev /config  
  
VOLUME ["/data", "/output", "/state", "/config"]  
WORKDIR /data  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["--lang"]  

