FROM postgres:9.5  
MAINTAINER Paulson McIntyre <paul+docker@gpmidi.net>  
MAINTAINER Rick White <rickatnight11@gmail.com>  
  
# Set DB params  
ENV POSTGRES_USER=musicbrainz  
ENV POSTGRES_PASSWORD=musicbrainz  
ENV POSTGRES_DB=initial  
ENV PGDATA=/data  
  
# OPTIONAL: Configure apt-get proxy  
#RUN echo 'Acquire::http::Proxy "http://PROXY:PORT";' >> /etc/apt/apt.conf  
# Deps  
RUN echo "deb http://http.us.debian.org/debian stable main contrib non-free" >
/etc/apt/sources.list.d/nonfree.list  
RUN apt-get update  
RUN apt-get install -y adduser sudo git unzip unrar \  
bash-completion wget vim build-essential \  
postgresql-server-dev-9.5 \  
postgresql-plperl-9.5 libjson-xs-perl libicu-dev \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# Install MusicBrainz pg extension  
RUN mkdir -p /opt/musicbrainz  
WORKDIR /opt/muzicbrainz  
RUN git clone git://github.com/metabrainz/postgresql-musicbrainz-unaccent.git  
RUN git clone git://github.com/metabrainz/postgresql-musicbrainz-collate.git  
WORKDIR /opt/muzicbrainz/postgresql-musicbrainz-unaccent  
RUN make && make install  
WORKDIR /opt/muzicbrainz/postgresql-musicbrainz-collate  
RUN make && make install  

