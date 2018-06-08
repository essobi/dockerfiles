FROM ubuntu:trusty  
  
# Add openstreetmap apt-sources  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends software-properties-common \  
&& add-apt-repository ppa:kakrueger/openstreetmap \  
&& apt-get update  
  
# Install renderd  
RUN apt-get install -y --no-install-recommends renderd  
  
ENV PGHOST database  
ENV PGUSER postgres  
  
COPY renderd.conf /etc/renderd.conf  
  
VOLUME /var/lib/mod_tile  
VOLUME /etc/mapnik-osm-carto-data  
  
EXPOSE 7654  
# TODO fix `docker run -it renderd` not reacting to ctrl+c  
ENTRYPOINT ["renderd", "-f"]  

