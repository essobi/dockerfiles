FROM debian:latest  
MAINTAINER mail@marc-richter.info  
  
# Do not install recommended or suggested packages  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends  
  
# Update APT cache upgrade system  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update ; apt-get dist-upgrade  
  
# Install needed packages  
RUN apt-get install -y build-essential zlib1g-dev curl bc file  
  
# Install Bacula client (https://itwiki.in-
telegence.net/display/intele/Bacula+-+Installation+und+Benutzung+bei+IN-
telegence)  
ADD http://www.bacula.org/downloads/Bacula-5.2.13/bacula-5.2.13.tar.gz
/usr/src/bacula-5.2.13.tar.gz  
RUN cd /usr/src && \  
tar xfz bacula-5.2.13.tar.gz || exit 1 && \  
rm -f bacula-5.2.13.tar.gz  
#RUN curl http://www.bacula.org/downloads/Bacula-5.2.13/bacula-5.2.13.tar.gz |
tar xfz - -C /usr/src/ || exit 1  
RUN cd /usr/src/bacula-5.2.13 && \  
./configure --enable-client-only --sysconfdir=/opt/bacula/etc
--sbindir=/opt/bacula/bin --mandir=/opt/bacula/man \  
\--bindir=/opt/bacula/bin --libexecdir=/opt/bacula/lib
--sharedstatedir=/opt/bacula/share \  
\--localstatedir=/opt/bacula/local/ --libdir=/opt/bacula/lib --enable-
smartalloc \  
\--with-working-dir=/opt/bacula/working --with-dir-password=baculapass --with-
fd-password=baculapass \  
\--with-sd-password=baculapass || exit 1 && \  
make || exit 1 && \  
make install || exit 1  
RUN cp /opt/bacula/etc/bacula-ctl-fd /etc/init.d/  
ADD files/bacula-fd.conf /opt/bacula/etc/bacula-fd.conf  
  
# Cleanup  
RUN rm -rf /var/cache/apt /var/lib/apt/lists  
  
# Add 'init' - script  
ADD files/init /opt/init  
RUN chmod 755 /opt/init  
  
EXPOSE 9102  
CMD ["/opt/init"]  

