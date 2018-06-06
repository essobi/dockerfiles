FROM debian:stable  
  
LABEL maintainer="Jaehoon Choi <plaintext@andromedarabbit.net>"  
  
ARG DEBIAN_FRONTEND  
ENV DEBIAN_FRONTEND=noninteractive  
  
ARG MAXSCALE_URL  
ONBUILD ENV
MAXSCALE_URL=http://downloads.mariadb.com/enterprise/4d7m-n51s/mariadb-
maxscale/latest/debian/dists/stretch/main/binary-
amd64/maxscale-2.1.9-1.debian.stretch.x86_64.deb  
  
# Setup base packages.  
ONBUILD RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends apt-utils \  
&& apt-get install -y --no-install-recommends curl \  
&& apt-get install -y --no-install-recommends libsqlite3-dev \  
&& apt-get install -y --no-install-recommends libssl1.1 \  
&& apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false  
  
ONBUILD RUN curl -o maxscale.deb ${MAXSCALE_URL}  
  
ONBUILD RUN dpkg -i maxscale.deb \  
&& rm maxscale.deb  
  
# Move configuration file in directory for exports  
ONBUILD RUN mkdir -p /etc/maxscale.d \  
&& cp /etc/maxscale.cnf.template /etc/maxscale.d/maxscale.cnf \  
&& ln -sf /etc/maxscale.d/maxscale.cnf /etc/maxscale.cnf  
  
# VOLUME for custom configuration  
VOLUME ["/etc/maxscale.d"]  
  
  
# EXPOSE the MaxScale default ports  
## RW Split Listener  
EXPOSE 4006  
  
## Read Connection Listener  
EXPOSE 4008  
  
## Debug Listener  
EXPOSE 4442  
  
## CLI Listener  
EXPOSE 6603  
  
# Running MaxScale  
ENTRYPOINT ["/usr/bin/maxscale", "-d"]  

