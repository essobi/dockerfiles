FROM debian:jessie  
  
RUN apt-get update && apt-get -y install libfontconfig wget adduser openssl
ca-certificates curl  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN arch="$(dpkg --print-architecture)" \  
&& set -x \  
&& curl -o /usr/local/bin/gosu -fSL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch" \  
&& curl -o /usr/local/bin/gosu.asc -fSL
"https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN addgroup --gid 30110 grafana  
RUN useradd -u 30110 -g grafana -s /bin/false grafana  
  
RUN wget http://grafanarel.s3.amazonaws.com/builds/grafana_2.1.0_amd64.deb  
  
RUN dpkg -i grafana_2.1.0_amd64.deb  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 3000  
# Mount this to make the grafana database persistent  
VOLUME ["/var/lib/grafana"]  
# Optional logging mount  
VOLUME ["/var/log/grafana"]  
  
VOLUME ["/etc/grafana"]  
  
WORKDIR /usr/share/grafana  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["grafana-server", "--config=/etc/grafana/grafana.ini",
"cfg:default.paths.data=/var/lib/grafana",
"cfg:default.paths.logs=/var/log/grafana"]  

