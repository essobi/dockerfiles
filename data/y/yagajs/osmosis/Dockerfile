FROM openjdk:latest  
  
MAINTAINER Arne Schubert <atd.schubert@gmail.com>  
  
ARG OSMOSIS_URL="http://bretth.dev.openstreetmap.org/osmosis-
build/osmosis-0.45.tgz"  
ENV OSMOSIS_URL $OSMOSIS_URL  
RUN set -x \  
&& useradd -ms /bin/bash osmosis \  
&& mkdir -p /opt/osmosis \  
&& curl $OSMOSIS_URL | tar xz -C /opt/osmosis \  
&& ln -s /opt/osmosis/bin/osmosis /usr/local/bin/osmosis  
  
USER osmosis  
CMD ["osmosis"]

