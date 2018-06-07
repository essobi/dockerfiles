FROM java:7  
MAINTAINER Jacob Blain Christen <jchristen@parchment.com>  
  
ENV HORNETQ_HOME=/usr/local/hornetq \  
HORNETQ_VERSION=2.2.14.Final  
  
ENV HORNETQ_GID=5445 \  
HORNETQ_GROUP=hornetq \  
HORNETQ_UID=5445 \  
HORNETQ_USER=hornetq  
  
COPY src/main/container/srv/ /srv/  
  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get --assume-yes --no-install-recommends install \  
libaio1 \  
&& mkdir -vp ${HORNETQ_HOME} \  
&& groupadd -g ${HORNETQ_GID} ${HORNETQ_GROUP} \  
&& useradd -d ${HORNETQ_HOME} -u ${HORNETQ_UID} -g ${HORNETQ_GID} -c "HornetQ
Runtime" ${HORNETQ_USER} \  
&& wget --progress=dot:mega -O-
"http://downloads.jboss.org/hornetq/hornetq-${HORNETQ_VERSION}.tar.gz" | tar
-xz --strip=1 -C "${HORNETQ_HOME}" \  
&& chown -R ${HORNETQ_USER}:${HORNETQ_GROUP} \  
${HORNETQ_HOME} \  
&& apt-get clean \  
&& rm -rf \  
/tmp/* \  
/var/tmp/* \  
/var/lib/apt/lists/* \  
&& find /srv/ -name "*.sh" | xargs chmod -v +x  
  
USER ${HORNETQ_USER}:${HORNETQ_GROUP}  
  
WORKDIR ${HORNETQ_HOME}  
  
EXPOSE 5445  
ENTRYPOINT ["/srv/hornetq.sh"]  
CMD ["hornetq"]

