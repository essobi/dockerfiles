FROM pygmy/postgres:9.6  
MAINTAINER Maciej Lisiewski <maciej.lisiewski@gmail.com>  
  
ARG REPMGR_VERSION=3.3.2  
ARG REPMGR_SHA1=48ed41fd552df50b597b547deccfecd8b12a5cf1  
  
RUN apk add --no-cache --virtual .build-deps \  
curl \  
make \  
gcc \  
postgresql-dev \  
libxslt-dev \  
libxml2-dev \  
libedit-dev \  
libc-dev \  
&& curl -sSL
https://github.com/2ndQuadrant/repmgr/archive/v${REPMGR_VERSION}.tar.gz -o
${REPMGR_VERSION}.tar.gz \  
&& echo "${REPMGR_SHA1} ${REPMGR_VERSION}.tar.gz" | sha1sum -c - \  
&& tar zxf ${REPMGR_VERSION}.tar.gz \  
&& cd repmgr-${REPMGR_VERSION} \  
&& make USE_PGXS=1 install \  
&& cd .. \  
&& rm -Rf repmgr-${REPMGR_VERSION} ${REPMGR_VERSION}.tar.gz \  
&& apk del .build-deps  
  
VOLUME /var/lib/postgresql/9.6/data  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]  
  
CMD ["postgres"]  

