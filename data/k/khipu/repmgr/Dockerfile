FROM khipu/base-alpine-s6  
MAINTAINER developers@khipu.com  
  
ARG REPMGR_VERSION=3.1.3  
ENV PG_VERSION 9.5  
ENV PATH /usr/lib/postgresql/$PG_VERSION/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
  
RUN apk add -U postgresql libxslt libxml2 libedit openssh-client rsync \  
&& rm -rf /var/cache/apk/*  
  
RUN apk add -U make gcc postgresql-dev libxslt-dev libxml2-dev libedit-dev
libc-dev \  
&& curl -sSL
https://github.com/2ndQuadrant/repmgr/archive/v${REPMGR_VERSION}.tar.gz -o
${REPMGR_VERSION}.tar.gz \  
&& tar xf ${REPMGR_VERSION}.tar.gz \  
&& cd repmgr-${REPMGR_VERSION} \  
&& make USE_PGXS=1 install \  
&& cd .. \  
&& rm -Rf repmgr-${REPMGR_VERSION} ${REPMGR_VERSION}.tar.gz \  
&& apk del make gcc libxslt-dev libxml2-dev libedit-dev postgresql-dev libc-
dev \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /etc/repmgr /var/lib/postgresql/.ssh \  
&& chmod 0700 /var/lib/postgresql/.ssh \  
&& chown postgres:postgres /var/lib/postgresql/.ssh  
  
COPY confd /etc/confd  
COPY s6/repmgr.sh /etc/services.d/repmgr/run  
COPY s6/postgres.sh /etc/services.d/postgres/run  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

