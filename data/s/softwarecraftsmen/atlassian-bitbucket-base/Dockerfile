FROM openjdk:8u141-jdk  
MAINTAINER Software Craftsmen GmbH & Co KG <office@software-craftsmen.at>  
  
ARG "version=unknown"  
ARG "build_date=unknown"  
ARG "commit_hash=unknown"  
ARG "vcs_url=unknown"  
ARG "vcs_branch=unknown"  
ARG "vcs_ref=unknown"  
LABEL org.label-schema.vendor="Software Craftsmen Gmbh & Co KG" \  
org.label-schema.name="Atlassian Bitbucket" \  
org.label-schema.description="Atlassian Bitbucket" \  
org.label-schema.usage="${vcs_url}" \  
org.label-schema.url="${vcs_url}" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$vcs_ref \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$build_date  
  
RUN if [ ! "${http_proxy}" = "" ] ; then echo "Acquire::http::Proxy
\"${http_proxy}\";" >> /etc/apt/apt.conf.d/98proxy; fi && \  
if [ ! "${https_proxy}" = "" ] ; then echo "Acquire::https::Proxy
\"${https_proxy}\";" >> /etc/apt/apt.conf.d/98proxy; fi && \  
if [ ! "${http_proxy}" = "" ] ; then echo "http_proxy=${http_proxy}" >>
/etc/wgetrc; fi && \  
if [ ! "${https_proxy}" = "" ] ; then echo "https_proxy=${https_proxy}" >>
/etc/wgetrc; fi  
  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
ENV BITBUCKET_HOME=/var/atlassian/application-data/bitbucket  
ENV BITBUCKET_INSTALL_DIR=/opt/atlassian/bitbucket  
ARG BITBUCKET_VERSION=5.4.0  
ARG
BITBUCKET_DOWNLOAD_URL=https://downloads.atlassian.com/software/stash/downloads/atlassian-
bitbucket-${BITBUCKET_VERSION}.tar.gz  
  
RUN apt-get update -qq && \  
update-ca-certificates && \  
apt-get install -y --no-install-recommends ca-certificates wget curl git ssh
bash procps openssl perl ttf-dejavu && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/lib/cache /var/lib/log /tmp/* /var/tmp/* && \  
mkdir -p ${BITBUCKET_HOME} ${BITBUCKET_HOME}/lib ${BITBUCKET_INSTALL_DIR}
${BITBUCKET_INSTALL_DIR}/lib && \  
curl -L --silent ${BITBUCKET_DOWNLOAD_URL} | tar -xz --strip-components=1 -C
"$BITBUCKET_INSTALL_DIR" && \  
chmod -R 700 ${BITBUCKET_HOME} ${BITBUCKET_INSTALL_DIR} && \  
chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_HOME} ${BITBUCKET_INSTALL_DIR}  
  
COPY bitbucket.properties ${BITBUCKET_HOME}/shared/bitbucket.properties  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY http-proxy.sh /http-proxy.sh  
RUN chmod a+x /docker-entrypoint.sh /http-proxy.sh && \  
chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_HOME}/shared  
  
WORKDIR ${BITBUCKET_HOME}  
  
USER ${RUN_USER}:${RUN_GROUP}  
  
# https://github.com/krallin/tini  
# This requires the docker run --init option for enabling tini!  
CMD ["/docker-entrypoint.sh", "-fg"]  
ENTRYPOINT ["/dev/init", "--"]  

