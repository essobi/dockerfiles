FROM shift/ubuntu:15.04  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
WORKDIR /tmp  
RUN apt-get update \  
&& apt-get install curl --yes \  
&& curl -L -O
https://grafanarel.s3.amazonaws.com/builds/grafana_2.5.0_amd64.deb \  
&& apt-get install -y adduser libfontconfig \  
&& dpkg -i grafana_2.5.0_amd64.deb \  
&& rm grafana_2.5.0_amd64.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3000  
WORKDIR /usr/share/grafana  
CMD ["/usr/sbin/grafana-server", "--pidfile=/var/run/grafana-server.pid", "--
config=/etc/grafana/grafana.ini", "cfg:default.paths.data=/var/lib/grafana",
"cfg:default.paths.logs=/var/log/grafana"]  

