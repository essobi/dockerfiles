FROM debian:jessie  
  
MAINTAINER Byte Pixie <hello@bytepixie.com>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
libssl1.0.0 \  
logrotate \  
curl \  
&& curl -L https://dzbscw1ubdtyw.cloudfront.net/actordb_0.10.25-1_amd64.deb -o
/tmp/actordb.deb \  
&& dpkg -i /tmp/actordb.deb \  
&& curl -L https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb -o /tmp/dumb-init.deb \  
&& dpkg -i /tmp/dumb-init.deb \  
&& apt-get purge --auto-remove -y \  
curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
#  
# Bootstrap scripts.  
COPY ./docker-config.sh ./docker-run.sh ./docker-entrypoint.sh /  
  
#  
# Default Thrift and MySQL client ports.  
EXPOSE 33306 33307  
#  
# Default RCP port.  
EXPOSE 44380  
EXPOSE 44370-44379  
#  
# Locations of data, config and logs.  
VOLUME /var/lib/actordb /etc/actordb /var/log/actordb  
#  
# Use dumb-init to make sure actordb is not running as PID 1.  
ENTRYPOINT ["dumb-init"]  
CMD ["/docker-entrypoint.sh"]  

