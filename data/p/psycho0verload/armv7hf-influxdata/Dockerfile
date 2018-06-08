FROM resin/armv7hf-debian-qemu  
  
RUN [ "cross-build-start" ]  
RUN apt-get update  
RUN apt-get -y install apt-utils  
RUN apt-get -y install wget  
  
RUN set -ex && \  
for key in \  
05CE15085FC09D18E99EFB22684A14CF2582E0C5 ; \  
do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" ; \  
done  
  
ENV CHRONOGRAF_VERSION 1.3.2.1  
RUN buildDeps='curl' \  
set -x && \  
apt-get update && apt-get install -y ca-certificates $buildDeps \--no-install-
recommends && \  
rm -rf /var/lib/apt/lists/* && \  
curl -SLO
"https://dl.influxdata.com/chronograf/releases/chronograf_${CHRONOGRAF_VERSION}_armhf.deb.asc"
&& \  
curl -SLO
"https://dl.influxdata.com/chronograf/releases/chronograf_${CHRONOGRAF_VERSION}_armhf.deb"
&& \  
gpg --batch --verify chronograf_${CHRONOGRAF_VERSION}_armhf.deb.asc
chronograf_${CHRONOGRAF_VERSION}_armhf.deb && \  
dpkg -i chronograf_${CHRONOGRAF_VERSION}_armhf.deb && \  
rm -f chronograf_${CHRONOGRAF_VERSION}_armhf.deb* && \  
apt-get purge -y --auto-remove $buildDeps  
  
COPY LICENSE /usr/share/chronograf/LICENSE  
COPY agpl-3.0.md /usr/share/chronograf/agpl-3.0.md  
  
RUN [ "cross-build-end" ]  
  
EXPOSE 8888  
VOLUME /var/lib/chronograf  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["chronograf"]  

