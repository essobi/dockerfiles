FROM openjdk:8u131-alpine  
  
COPY docker/ /  
  
# Bitbucket envs  
ENV BITBUCKET_USER=bitbucket \  
BITBUCKET_UID=1591 \  
BITBUCKET_GROUP=bitbucket \  
BITBUCKET_GID=1591 \  
BITBUCKET_HOME=/var/atlassian/application-data/bitbucket \  
BITBUCKET_INSTALL_DIR=/opt/atlassian/bitbucket \  
BITBUCKET_VERSION=5.2.2  
# User settings  
RUN mkdir -p ${BITBUCKET_HOME} \  
&& addgroup \  
-g ${BITBUCKET_GID} \  
-S ${BITBUCKET_GROUP} \  
&& adduser \  
-u ${BITBUCKET_UID} \  
-D -S \  
-h ${BITBUCKET_HOME} \  
-G ${BITBUCKET_GROUP} ${BITBUCKET_USER} \  
# persistent deps  
&& apk add \--no-cache --virtual .persistent-deps \  
bash \  
ca-certificates \  
curl \  
git \  
#mini-sendmail \  
openssh \  
openssl \  
perl \  
procps \  
# install dumb-init https://github.com/Yelp/dumb-init  
&& curl -sL https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 -o /usr/local/bin/dumb-init \  
&& chmod +x /usr/local/bin/dumb-init \  
# install Bitbucket  
&& mkdir -p ${BITBUCKET_INSTALL_DIR} \  
&& curl -sL
https://downloads.atlassian.com/software/stash/downloads/atlassian-
bitbucket-${BITBUCKET_VERSION}.tar.gz | tar -xz --strip-components=1 -C
"${BITBUCKET_INSTALL_DIR}" \  
&& chown -R ${BITBUCKET_USER}:${BITBUCKET_GROUP} ${BITBUCKET_INSTALL_DIR}/  
  
# HTTP & SSH Port  
EXPOSE 7990 7999  
WORKDIR ${BITBUCKET_HOME}  
  
ENTRYPOINT [ "dumb-init" ]  
  
CMD [ "docker-entrypoint", "-fg" ]  

