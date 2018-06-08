FROM ubuntu:bionic  
  
# Set time zone  
ENV TZ 'UTC'  
RUN echo $TZ > /etc/timezone  
  
# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.  
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d  
  
# Create directories  
RUN mkdir -p /var/azuracast/servers/shoutcast2 && \  
mkdir -p /var/azuracast/servers/icecast2 && \  
mkdir -p /var/azuracast/servers/station-watcher && \  
mkdir -p /var/azuracast/stations  
  
RUN adduser --home /var/azuracast --disabled-password --gecos "" azuracast &&
\  
chown -R azuracast:azuracast /var/azuracast  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -q -y wget curl git vim libssl-
dev \  
libcurl4-openssl-dev gcc pkg-config  
  
# Install supervisord  
RUN mkdir -p /var/log/supervisor  
  
RUN apt-get update && \  
apt-get install -q -y supervisor  
  
ADD ./supervisord.conf /etc/supervisor/supervisord.conf  
  
# Download Shoutcast 2  
WORKDIR /var/azuracast/servers/shoutcast2  
  
RUN wget
http://download.nullsoft.com/shoutcast/tools/sc_serv2_linux_x64-latest.tar.gz
&& \  
tar -xzf sc_serv2_linux_x64-latest.tar.gz  
  
# Download and build IceCast-KH  
WORKDIR /var/azuracast/servers/icecast2  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
libxml2 \  
libxslt1-dev libvorbis-dev && \  
wget https://github.com/karlheyes/icecast-kh/archive/icecast-2.4.0-kh7.tar.gz
&& \  
tar --strip-components=1 -xzf icecast-2.4.0-kh7.tar.gz && \  
./configure && \  
make && \  
make install  
  
ADD ./error.mp3 /usr/local/share/icecast/web/error.mp3  
ADD ./status-json.xsl /usr/local/share/icecast/web/status-json.xsl  
ADD ./xml2json.xslt /usr/local/share/icecast/web/xml2json.xslt  
  
# Build LiquidSoap  
# For libfdk-aac-dev  
RUN sed -e 's#main#main contrib non-free#' -i /etc/apt/sources.list  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
ocaml rsync opam \  
libpcre3-dev libfdk-aac-dev libmad0-dev libmp3lame-dev libtag1-dev libfaad-dev
libflac-dev \  
libogg-dev libopus-dev m4 aspcud camlp4  
  
USER azuracast  
  
RUN opam init -y && \  
opam install -y taglib.0.3.3 mad.0.4.5 faad.0.3.3 fdkaac.0.2.1 lame.0.3.3
vorbis.0.7.0 cry.0.6.0 \  
opus.0.1.2 flac.0.1.2 liquidsoap.1.3.3  
  
# Install Python and pull the station-watcher app  
USER root  
  
WORKDIR /var/azuracast/servers/station-watcher  
COPY ./station-watcher ./station-watcher  
  
RUN chown azuracast:azuracast ./station-watcher \  
&& chmod a+x ./station-watcher  
  
WORKDIR /root  
  
EXPOSE 9001  
EXPOSE 8000-8500  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

