ARG SONARQUBE_VERSION="lts-alpine"  
FROM sonarqube:${SONARQUBE_VERSION}  
MAINTAINER Software Craftsmen GmbH und CoKG <office@software-craftsmen.at>  
  
ARG version="unknown"  
ARG build_date="unknown"  
ARG commit_hash="unknown"  
ARG vcs_url="unknown"  
ARG vcs_branch="unknown"  
ARG vcs_ref="unknown"  
LABEL org.label-schema.vendor="Software Craftsmen Gmbh & Co KG" \  
org.label-schema.name="sonarqube-server" \  
org.label-schema.description="sonarqube-server" \  
org.label-schema.usage="${vcs_url}" \  
org.label-schema.url="${vcs_url}" \  
org.label-schema.vcs-url=$vcs_url \  
org.label-schema.vcs-branch=$vcs_branch \  
org.label-schema.vcs-ref=$vcs_ref \  
org.label-schema.version=$version \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$build_date  
  
ENV SONARQUBE_HOME /opt/sonarqube  
  
RUN if [ ! "${http_proxy}" = "" ] ; then echo "Acquire::http::Proxy
\"${http_proxy}\";" >> /etc/apt/apt.conf.d/98proxy; fi && \  
if [ ! "${https_proxy}" = "" ] ; then echo "Acquire::https::Proxy
\"${https_proxy}\";" >> /etc/apt/apt.conf.d/98proxy; fi && \  
if [ ! "${http_proxy}" = "" ] ; then echo "http_proxy=${http_proxy}" >>
/etc/wgetrc; fi && \  
if [ ! "${https_proxy}" = "" ] ; then echo "https_proxy=${https_proxy}" >>
/etc/wgetrc; fi  
  
COPY install-plugin.sh /install-plugin.sh  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh && \  
bash -c "source /install-plugin.sh && \  
installPlugin sonar-groovy-plugin 1.4 && \  
installPlugin sonar-java-plugin 4.5.0.8398"  
  
ENTRYPOINT /docker-entrypoint.sh  

