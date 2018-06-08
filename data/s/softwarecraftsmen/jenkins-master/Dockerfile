ARG JENKINS_VERSION="lts-alpine"  
FROM jenkinsci/jenkins:${JENKINS_VERSION}  
MAINTAINER Software Craftsmen GmbH und CoKG <office@software-craftsmen.at>  
  
ARG version="unknown"  
ARG build_date="unknown"  
ARG commit_hash="unknown"  
ARG vcs_url="unknown"  
ARG vcs_branch="unknown"  
ARG vcs_ref="unknown"  
LABEL org.label-schema.vendor="Software Craftsmen Gmbh & Co KG" \  
org.label-schema.name="jenkins-master" \  
org.label-schema.description="Jenkins Master" \  
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
  
USER jenkins  
  
COPY *.groovy /usr/share/jenkins/ref/init.groovy.d/  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt &&
\  
echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  

