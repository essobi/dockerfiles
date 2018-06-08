FROM debian:latest  
  
RUN apt-get --assume-yes update  
RUN apt-get --assume-yes install libdevice-serialport-perl libjson-perl
libany-uri-escape-perl  
  
ENV FHEM_HOME /opt/fhem  
  
# FHEM is ran with user `fhem`, uid = 1000  
# If you bind mount a volume from host/volume from a data container,  
# ensure you use same uid  
RUN useradd -d "$FHEM_HOME" -u 1000 -m -s /bin/bash fhem  
  
# Add Tini  
ENV TINI_VERSION v0.8.3  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/bin/tini  
RUN chmod +x /bin/tini  
  
ADD http://www.dhs-computertechnik.de/downloads/fhem-cvs.tgz
/usr/local/lib/fhem.tgz  
RUN cd /opt && tar xvzf /usr/local/lib/fhem.tgz && mv fhem fhem-svn && mkdir
/opt/fhem && chown fhem:fhem /opt/fhem  
  
# FHEM home directoy is a volume, so configuration and build history  
# can be persisted and survive image upgrades  
VOLUME /opt/fhem  
  
EXPOSE 7072 8083 8084 8085  
COPY fhem.sh /usr/local/bin/fhem.sh  
RUN chmod a+x /usr/local/bin/fhem.sh  
  
USER fhem  
  
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/fhem.sh"]  

