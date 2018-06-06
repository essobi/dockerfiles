FROM debian:jessie  
  
MAINTAINER Kalle R. Møller <docker@k-moeller.dk>  
  
ARG DEBIAN_FRONTEND=noninteractive  
ARG S6_VERSION=v1.18.1.5  
RUN apt-get update -q -y \  
&& apt-get install -q -y --no-install-recommends curl ca-certificates \  
&& curl -L -o /tmp/s6-overlay-amd64.tar.gz "https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz"
\  
&& tar xzf /tmp/s6-overlay-amd64.tar.gz -C / \  
&& apt-get --purge autoremove curl ca-certificates -q -y \  
&& apt-get clean -q -y  
  
RUN apt-get update -q -y \  
&& apt-get install -q -y --no-install-recommends \  
cron  
  
COPY rotate /bin/rotate  
COPY run /etc/services.d/cron/run  
  
RUN \  
chmod +x /bin/rotate \  
&& echo '*/15 * * * * root /bin/rotate 2>&1' > /etc/cron.d/hello-cron \  
&& echo '' >> /etc/cron.d/hello-cron \  
&& chmod +x /etc/cron.d/hello-cron \  
&& touch /var/log/cron.log  
  
ENTRYPOINT ["/init"]  
  
CMD ["tail", "-f", "/var/log/cron.log"]  

