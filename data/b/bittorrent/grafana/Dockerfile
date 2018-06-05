FROM debian:jessie  
  
ENV GRAFANA_VERSION=4.2.0  
ENV GRAFANA_DOWNLOAD_URL=https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana_${GRAFANA_VERSION}_amd64.deb  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install libfontconfig curl ca-certificates
&& \  
apt-get clean && \  
curl ${GRAFANA_DOWNLOAD_URL} > /tmp/grafana.deb && \  
dpkg -i /tmp/grafana.deb && \  
rm /tmp/grafana.deb && \  
curl -L https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64 >
/usr/sbin/gosu && \  
chmod +x /usr/sbin/gosu && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3000  
  
COPY ./run.sh /run.sh  
COPY ./grafana-default-config /grafana-default-config  
  
ENTRYPOINT ["/run.sh"]  

