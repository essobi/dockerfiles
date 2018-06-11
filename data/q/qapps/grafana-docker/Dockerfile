FROM debian:jessie  
  
MAINTAINER Yury Kavaliou qualiapps@gmail.com  
  
ENV GRAFANA_VERSION 2.5.0  
ENV GRAFANA_SCR /opt/grafana/  
  
RUN apt-get update && \  
apt-get -y install libfontconfig wget adduser openssl ca-certificates python
python-pip && \  
apt-get clean && \  
pip install requests && \  
wget
https://grafanarel.s3.amazonaws.com/builds/grafana_${GRAFANA_VERSION}_amd64.deb
-O /tmp/grafana.deb && \  
dpkg -i /tmp/grafana.deb && \  
rm /tmp/grafana.deb  
  
VOLUME ["/var/lib/grafana", "/var/log/grafana", "/etc/grafana"]  
  
COPY ./files/start.py ${GRAFANA_SCR}start.py  
RUN chmod +x ${GRAFANA_SCR}start.py  
  
EXPOSE 3000  
ENTRYPOINT ["/opt/grafana/start.py"]

