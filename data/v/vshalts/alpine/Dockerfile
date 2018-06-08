FROM frolvlad/alpine-glibc:alpine-3.4  
MAINTAINER Vadim Shalts <vshalts@gmail.com>  
  
RUN mkdir /app && chown nobody:nobody /app  
WORKDIR /app  
  
ENV DUMB_INIT_VERSION=1.2.0  
RUN apk add --update ca-certificates curl binutils && \  
curl -O -L https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 && \  
mv dumb-init_${DUMB_INIT_VERSION}_amd64 /usr/local/bin/dumb-init && \  
chmod +x /usr/local/bin/dumb-init && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*  
  
COPY dpkg /usr/bin/dpkg  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
  
# USER nobody  

