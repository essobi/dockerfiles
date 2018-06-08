### Dockerfile for splunk  
### Originally from dmaxwell351/docker-containers and splunk/docker-splunk  
FROM phusion/baseimage:0.10.0  
LABEL maintainer="jtok"  
  
# Set environment variables  
ENV HOME=/root  
ENV SPLUNK_HOME=/opt/splunk  
ENV DEBIAN_FRONTEND=noninteractive  
ENV LC_ALL=C.UTF-8  
ENV LANG=en_US.UTF-8  
ENV LANGUAGE=en_US.UTF-8  
ENV SPLUNK_PRODUCT=splunk  
ENV SPLUNK_VERSION=7.0.2  
ENV SPLUNK_BUILD=03bbabbd5c0f  
ENV SPLUNK_FILENAME=splunk-${SPLUNK_VERSION}-${SPLUNK_BUILD}-Linux-x86_64.tgz  
ENV SPLUNK_BACKUP_DEFAULT_ETC=/var/opt/splunk  
ENV SPLUNK_START_ARGS="--accept-license --answer-yes --no-prompt"  
# Use Phusion's init system.  
CMD ["/sbin/my_init"]  
  
# Configure user nobody to match unRAID's settings  
RUN usermod -u 99 nobody && \  
usermod -g 100 nobody && \  
usermod -d /home nobody && \  
chown -R nobody:users /home  
  
ENV SPLUNK_USER nobody  
ENV SPLUNK_GROUP users  
  
# Install tzdata and set timezone environment variable  
RUN apt update && apt install -y tzdata \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV TZ=America/Chicago  
  
# Make the "en_US.UTF-8" locale so Splunk will be utf-8 enabled by default  
RUN apt-get update -q \  
&& apt-get install -y --no-install-recommends apt-utils \  
&& apt-get install -y locales \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
# pdfgen dependency  
RUN apt-get update -q \  
&& apt-get install -y libgssapi-krb5-2 \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install sudo  
RUN apt-get update -q \  
&& apt-get install -y sudo \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install wget  
RUN apt-get update -q \  
&& apt-get install -y wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Splunk and remove wget  
RUN mkdir -p ${SPLUNK_HOME} \  
&& wget -O /tmp/${SPLUNK_FILENAME}
https://download.splunk.com/products/${SPLUNK_PRODUCT}/releases/${SPLUNK_VERSION}/linux/${SPLUNK_FILENAME}
\  
&& tar xzf /tmp/${SPLUNK_FILENAME} \--strip 1 -C ${SPLUNK_HOME} \  
&& rm /tmp/${SPLUNK_FILENAME} \  
&& apt-get purge -y --auto-remove wget \  
&& mkdir -p ${SPLUNK_BACKUP_DEFAULT_ETC} \  
&& cp -R ${SPLUNK_HOME}/etc ${SPLUNK_BACKUP_DEFAULT_ETC} \  
&& rm -fR ${SPLUNK_HOME}/etc \  
&& chown -R nobody:users ${SPLUNK_HOME} \  
&& chown -R nobody:users ${SPLUNK_BACKUP_DEFAULT_ETC} \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy entrypoint script  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod +x /sbin/entrypoint.sh  
  
# Set up ports for Web UI, Daemon, Indexing, and Syslog  
EXPOSE 8000/tcp 8089/tcp 9997/tcp 514/udp  
  
WORKDIR /opt/splunk  
  
VOLUME ["/opt/splunk/var", "/opt/splunk/etc", "/data", "/license"]  
  
HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["start-service"]  
  
### END  
### To make this a persistent container, you must map /opt/splunk/var and
/opt/splunk/etc of this container  
### to a folder on your host machine.  
###

