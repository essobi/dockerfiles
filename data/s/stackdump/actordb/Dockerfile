FROM debian:jessie  
  
MAINTAINER Byte Pixie <hello@bytepixie.com>  
  
RUN apt-get update \  
#  
# Install dependencies and curl (for geting release).  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
libssl1.0.0 \  
logrotate \  
curl \  
#  
# Install ActorDB.  
&& curl -L https://dzbscw1ubdtyw.cloudfront.net/actordb_0.10.24-1_amd64.deb -o
/tmp/actordb.deb \  
&& dpkg -i /tmp/actordb.deb \  
#  
# Install dumb-init (to handle PID 1 correctly).  
# https://github.com/Yelp/dumb-init  
&& curl -L https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-
init_1.1.3_amd64.deb -o /tmp/dumb-init.deb \  
&& dpkg -i /tmp/dumb-init.deb \  
#  
# Clean up temp stuff.  
&& apt-get purge --auto-remove -y \  
curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
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
CMD ["actordb", "foreground"]  

