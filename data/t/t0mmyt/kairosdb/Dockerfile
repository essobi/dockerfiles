FROM t0mmyt/jre8:latest  
MAINTAINER Tom Taylor <tom+dockerfiles@tomm.yt>  
  
EXPOSE 8080 4242  
ENV VER=1.1.3  
ENV REL=1  
ENV
URL=https://github.com/kairosdb/kairosdb/releases/download/v${VER}/kairosdb-${VER}-${REL}.tar.gz  
ENV DUMB_INIT=https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64  
  
RUN curl -Ls ${URL} | tar zx -C /opt && \  
curl -Ls ${DUMB_INIT} > /dumb-init && chmod 755 /dumb-init && \  
apt-get -yqq install netcat  
COPY kairosdb.properties /opt/kairosdb/conf/  
COPY go.sh /  
  
WORKDIR /opt/kairosdb  
ENTRYPOINT ["/dumb-init", "/go.sh"]  

