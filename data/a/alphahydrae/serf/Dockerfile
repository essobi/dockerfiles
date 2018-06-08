FROM alpine:3.5  
LABEL maintainer="docker@alphahydrae.com"  
  
ENV SERF_VERSION="0.8.1"  
ENV S6_OVERLAY_VERSION="v1.17.2.0"  
# Install curl and gzip  
RUN apk add --update curl gzip && \  
rm -rf /var/cache/apk/*  
  
# Install s6 for service supervision: https://github.com/just-
containers/s6-overlay  
RUN curl -sSLo /tmp/s6.tar.gz https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz && \  
tar xzf /tmp/s6.tar.gz -C / && \  
rm -f /tmp/s6.tar.gz  
  
# Install serf  
RUN curl -sSLo /tmp/serf.gz
https://releases.hashicorp.com/serf/${SERF_VERSION}/serf_${SERF_VERSION}_linux_amd64.zip
\  
&& gunzip -c /tmp/serf.gz > /usr/local/bin/serf \  
&& chmod 755 /usr/local/bin/serf \  
&& rm -f /tmp/serf.gz  
  
# Add s6 configuration  
ADD cont-finish.d /etc/cont-finish.d/  
ADD services.d /etc/services.d/  
  
# Add serf configuration  
ADD serf.conf /etc/serf.conf  
  
# Set s6 as the entrypoint  
ENTRYPOINT ["/init"]  

