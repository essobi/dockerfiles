FROM debian:jessie-slim  
  
ENV version=4.2.0 uid=2007  
ENV DISPLAY=":0" LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive  
  
LABEL maintainer="Ian Martin <ian@imartin.net>" license="MIT" version=$version  
  
COPY ./run.sh /run.sh  
  
RUN apt-get update && apt-get install -y curl && \  
rm -rf /var/lib/apt/lists/* && \  
useradd --create-home --uid $uid grafana && \  
passwd -l grafana && \  
curl -LO https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana-${version}.linux-x64.tar.gz && \  
tar xzf grafana-${version}.linux-x64.tar.gz -C / && \  
mv /grafana-${version} /grafana && \  
mkdir -p /grafana/data && \  
rm -f /grafana-${version}.linux-x64.tar.gz && \  
chown -R ${uid}:${uid} /grafana  
  
WORKDIR /grafana  
USER $uid  
  
EXPOSE 3000  
VOLUME ["/grafana/data"]  
  
ENTRYPOINT ["/run.sh"]  

