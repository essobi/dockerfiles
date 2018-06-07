FROM ubuntu:14.04  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ trusty universe' >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get -y install libfontconfig wget adduser  
  
RUN wget http://grafanarel.s3.amazonaws.com/builds/grafana_latest_amd64.deb
--no-check-certificate  
  
RUN dpkg -i grafana_latest_amd64.deb  
  
EXPOSE 3000  
ENTRYPOINT ["/usr/sbin/grafana-server", "--homepath=/usr/share/grafana", "--
config=/etc/grafana/grafana.ini", "cfg:default.paths.data=/var/lib/grafana",
"cfg:default.paths.logs=/var/log/grafana"]

