FROM haproxy:1.8.9  
ARG CONFD_VERSION=0.16.0  
ARG
CONFD_SHA256=255d2559f3824dd64df059bdc533fd6b697c070db603c76aaf8d1d5e6b0cc334  
  
ENV REFRESH_INTERVAL=300  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get install -y curl rsync procps \  
&& apt-get clean \  
&& rm -rf /var/apt/lists/*  
  
RUN curl -L -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd  
RUN echo "${CONFD_SHA256} /usr/local/bin/confd" | sha256sum -c -  
  
RUN mkdir -p /etc/confd/basic/conf.d /etc/confd/basic/templates/  
RUN mkdir -p /etc/confd/dynamic-routing/conf.d /etc/confd/dynamic-
routing/templates/  
COPY ./templates /templates  
COPY ./templates/reverse-proxy.toml /etc/confd/basic/conf.d/  
COPY ./templates/reverse-proxy.toml /etc/confd/dynamic-routing/conf.d/  
RUN cat /templates/common/* /templates/basic/* >
/etc/confd/basic/templates/reverse-proxy.cfg.tmpl  
RUN cat /templates/common/* /templates/dynamic-routing/* > /etc/confd/dynamic-
routing/templates/reverse-proxy.cfg.tmpl  
  
CMD /usr/local/bin/confd -interval $REFRESH_INTERVAL
-confdir=/etc/confd/$HAPROXY_CONFD_TMPL/ -backend rancher -prefix /2016-07-29  

