# Dockerfile to run the JKA demo site python services  
FROM ubuntu:16.04  
MAINTAINER Dan Padgett <dumbledore3@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
locales \  
python \  
python-falcon \  
python-dateutil \  
python-tz \  
python-pymongo \  
python-mpmath \  
python-pip \  
libjansson4 \  
lighttpd \  
zip && \  
pip install trueskill && \  
apt-get remove --purge --auto-remove -y python-pip && apt-get clean && apt-get
autoclean  
  
RUN cp /usr/share/i18n/charmaps/CP1252.gz /tmp && \  
cd /tmp && \  
gzip -d CP1252.gz && \  
localedef -f /tmp/CP1252 -i /usr/share/i18n/locales/en_US
/usr/lib/locale/en_US.CP1252  
  
RUN cp /usr/share/i18n/charmaps/UTF-8.gz /tmp && \  
cd /tmp && \  
gzip -d UTF-8.gz && \  
localedef -f /tmp/UTF-8 -i /usr/share/i18n/locales/en_US
/usr/lib/locale/en_US.UTF-8  
  
RUN lighttpd-enable-mod cgi  
  
RUN useradd -ms /bin/bash pyservices  
  
# copy the nice dotfiles that dockerfile/ubuntu gives us:  
RUN cd && cp -R .bashrc .profile /home/pyservices  
  
COPY python/* /home/pyservices/  
  
WORKDIR /home/pyservices  
  
RUN chown -R pyservices:pyservices /home/pyservices  
  
USER pyservices  
ENV HOME /home/pyservices  
ENV USER pyservices  
  
CMD lighttpd -D -f /home/pyservices/lighttpd.conf  

