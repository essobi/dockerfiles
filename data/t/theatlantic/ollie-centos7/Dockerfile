FROM centos:centos7  
  
MAINTAINER The Atlantic Programmers <programmers@theatlantic.com>  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REV  
ENV VCS_URL git@github.com:theatlantic/ollie-docker-containers.git  
  
LABEL org.label-schema.name="ollie-centos7" \  
org.label-schema.description="Ollie CentOS 7 base container" \  
org.label-schema.vendor="The Atlantic" \  
org.label-schema.version="$VERSION" \  
org.label-schema.vcs-url="$VCS_URL" \  
org.label-schema.license="BSD-2" \  
org.label-schema.schema-version="1.2"  
  
# Allow scripts to detect we're running in our own container  
RUN touch /ollie-centos7-container  
  
# add our user and group first to make sure their IDs get assigned  
# consistently, regardless of whatever dependencies get added  
RUN groupadd -g 509 deploy && useradd -m -u 508 -g 509 -G deploy deploy  
  
# Set the locale.  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN cd /usr/lib/locale \  
&& localedef --list-archive | grep -v -i ^en \  
| xargs localedef --delete-from-archive \  
&& localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& mv -f locale-archive locale-archive.tmpl \  
&& build-locale-archive  
  
ENV THEATLANTIC_RELEASE_RPM "http://dev.theatlantic.com/repo/el/7/x86_64/"\  
"packages/theatlantic-release-7-1.noarch.rpm"  
# Use openshift epel mirror, because it doesn't have constant syncing  
# race-condition errors  
RUN curl -SLv -o /etc/yum.repos.d/epel7.repo
https://mirror.openshift.com/mirror/epel/epel7.repo  
  
RUN yum update -y --setopt=tsflags=nodocs \  
&& yum install -y --setopt=tsflags=nodocs "${THEATLANTIC_RELEASE_RPM}" \  
&& yum clean all  
  
# add gosu for easy step-down from root  
ENV GOSU_VERSION 1.10  
RUN yum update -y --setopt=tsflags=nodocs \  
&& yum install -y --setopt=tsflags=nodocs dpkg \  
&& curl -SLv -o /usr/bin/gosu \  
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture)" \  
&& chmod +x /usr/bin/gosu \  
&& /usr/bin/gosu nobody true \  
&& yum erase -y dpkg \  
&& yum clean all  
  
ENV DOCKERIZE_VERSION 0.3.0  
RUN curl -SL \  
"https://github.com/jwilder/dockerize/releases/download/v$DOCKERIZE_VERSION/"\  
"dockerize-linux-amd64-v$DOCKERIZE_VERSION.tar.gz" \  
| tar -xzC /usr/bin  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN mkdir -p /mnt/{home,vols} && chown -R deploy:deploy /mnt  
  
VOLUME ["/mnt/home", "/mnt/vols"]  
  
ADD ps1.sh /etc/profile.d/ps1.sh  
  
LABEL org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.vcs-rev="$VCS_REV"  

