FROM alpine:3.6  
# Lifted from https://github.com/jojomi/docker-
hugo/blob/b03d1d0ad820bb42d1ecfdfa6aaaa6dad9772bae/Dockerfile#L5-L10  
ENV HUGO_VERSION=0.26  
ADD
https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
/tmp  
RUN cd /tmp && tar -xzvf hugo_*.tar.gz && \  
mkdir -p /usr/local/sbin \  
&& mv /tmp/hugo /usr/local/sbin/hugo  
  
RUN /usr/local/sbin/hugo version  
  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

