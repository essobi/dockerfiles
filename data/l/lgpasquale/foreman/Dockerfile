FROM debian:stable  
MAINTAINER Luca Pasquale  
  
# Ensures apt doesn't ask us silly questions:  
ENV DEBIAN_FRONTEND noninteractive  
  
# Add the Foreman repos  
RUN apt-get -y update && apt-get -y install wget  
RUN echo "deb http://deb.theforeman.org/ jessie 1.11" >
/etc/apt/sources.list.d/foreman.list  
RUN echo "deb http://deb.theforeman.org/ plugins 1.11" >>
/etc/apt/sources.list.d/foreman.list  
RUN wget -q http://deb.theforeman.org/pubkey.gpg -O- | apt-key add -  
RUN apt-get -y update && apt-get -y install foreman-installer  
# Not needed, but speeds up the first run of the container  
RUN apt-get -y update && apt-get -y install foreman foreman-pgsql foreman-
libvirt postgresql  
  
RUN apt-get -y install locales && \  
echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Copy our init.sh script into the container:  
COPY init.sh /usr/local/bin/init.sh  
RUN chmod a+x /usr/local/bin/init.sh  
  
VOLUME /etc/foreman  
VOLUME /etc/foreman-proxy  
VOLUME /etc/postgresql  
VOLUME /var/lib/foreman  
VOLUME /var/lib/puppet  
VOLUME /var/lib/postgresql  
  
# Expose TFTP port:  
EXPOSE 69/udp  
# Expose our HTTP/HTTPS ports:  
EXPOSE 80  
EXPOSE 443  
# Expose puppet port:  
EXPOSE 8140  
CMD ["/usr/local/bin/init.sh"]  
  

