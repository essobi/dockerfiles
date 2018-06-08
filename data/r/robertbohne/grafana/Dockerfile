FROM debian:jessie  
  
# Default for docker hub build  
ARG DOWNLOAD_URL=https://s3-us-west-2.amazonaws.com/grafana-
releases/master/grafana_latest_amd64.deb  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install libfontconfig curl ca-certificates
&& \  
apt-get clean && \  
curl ${DOWNLOAD_URL} > /tmp/grafana.deb && \  
dpkg -i /tmp/grafana.deb && \  
rm /tmp/grafana.deb && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
chmod -R g+w /var/lib/grafana && \  
chmod -R g+w /var/log/grafana && \  
chmod -R g+w /etc/grafana && \  
chgrp -R root /var/lib/grafana && \  
chgrp -R root /var/log/grafana && \  
chgrp -R root /etc/grafana  
  
ADD libnss_wrapper.so.0.2.3 /usr/local/lib/  
  
VOLUME ["/var/lib/grafana", "/var/log/grafana"]  
  
EXPOSE 3000  
  
COPY ./run.sh /run.sh  
  
USER 1001  
  
ENTRYPOINT ["/run.sh"]  

