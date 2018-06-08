FROM debian:jessie  
  
ENV GRAFANA_VERSION 4.6.3  
RUN apt-get update \  
&& apt-get install -y unzip libfontconfig wget adduser openssl ca-certificates
\  
&& wget https://s3-us-west-2.amazonaws.com/grafana-
releases/release/grafana_${GRAFANA_VERSION}_amd64.deb \  
&& dpkg -i grafana_${GRAFANA_VERSION}_amd64.deb  
  
EXPOSE 3000  
VOLUME ["/var/lib/grafana"]  
VOLUME ["/var/log/grafana"]  
VOLUME ["/etc/grafana"]  
  
WORKDIR /usr/share/grafana  
  
ENTRYPOINT ["/usr/sbin/grafana-server"]  
CMD [ \  
"--config", \  
"/etc/grafana/grafana.ini", \  
"cfg:default.paths.data=/var/lib/grafana", \  
"cfg:default.paths.logs=/var/log/grafana", \  
"cfg:default.paths.plugins=/var/lib/grafana/plugins" \  
]  

