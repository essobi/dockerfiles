FROM openjdk:8u121-alpine  
MAINTAINER Roman v. Gemmeren <strowi@hasnoname.de>  
  
ARG BITBUCKET_VERSION=5.3.1  
ARG
DOWNLOAD_URL=https://downloads.atlassian.com/software/stash/downloads/atlassian-
bitbucket-${BITBUCKET_VERSION}.tar.gz  
  
ARG POSTGRES_DRIVER_VERSION=42.1.1  
ARG MYSQL_DRIVER_VERSION=5.1.38  
# Setup useful environment variables  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
ENV BITBUCKET_HOME /var/atlassian/bitbucket  
ENV BITBUCKET_INSTALL /opt/atlassian/bitbucket  
  
RUN apk --update --no-cache add \  
tzdata \  
ca-certificates \  
wget \  
curl \  
git \  
openssh \  
bash \  
procps \  
openssl \  
perl \  
ttf-dejavu \  
tini \  
&& cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime \  
&& echo "Europe/Berlin" > /etc/timezone \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/* \  
&& update-ca-certificates \  
&& mkdir -p ${BITBUCKET_INSTALL} \  
&& curl -L --silent ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C
"$BITBUCKET_INSTALL" \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_INSTALL}/ \  
# Update the Postgres library to allow non-archaic Postgres versions \  
&& cd "${BITBUCKET_INSTALL}/app/WEB-INF/lib" \  
&& rm -f "./postgresql-9.*" \  
&& curl -Os
"https://jdbc.postgresql.org/download/postgresql-${POSTGRES_DRIVER_VERSION}.jar"
\  
# Add MySQL library \  
&& curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.tar.gz" \  
| tar -xz --directory "${BITBUCKET_INSTALL}/app/WEB-INF/lib" \  
\--strip-components=1 --no-same-owner \  
"mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar"  
  
# Expose HTTP and SSH ports  
# + set volumes/workdir  
EXPOSE 7990  
EXPOSE 7999  
VOLUME ["${BITBUCKET_HOME}"]  
WORKDIR $BITBUCKET_HOME  
  
ADD src/ /  
  
CMD ["/docker-entrypoint.sh", "-fg"]  
ENTRYPOINT ["/sbin/tini", "--"]  

