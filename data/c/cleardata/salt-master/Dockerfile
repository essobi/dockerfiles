FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y dist-upgrade && apt-get install -y software-
properties-common python-software-properties python curl git upstart python-
pip sysv-rc && rm -rf /var/lib/apt/lists/*  
RUN curl -L https://raw.githubusercontent.com/admgre/salt-
bootstrap/develop/bootstrap-salt.sh | sh -s -- -M -N -X -D -U -d git 2015.2 &&
rm -rf /var/lib/apt/lists/*  
EXPOSE 4505 4506  
VOLUME ["/etc/salt", "/srv/salt", "/srv/pillar", "/var/log/salt",
"/var/run/salt", "/var/cache/salt"]  
ENTRYPOINT ["/usr/bin/salt-master"]  

