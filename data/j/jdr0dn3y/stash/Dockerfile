# Basics  
#  
FROM jdr0dn3y/dev-studio-base  
MAINTAINER Justin Donnaruma <justin@rumatec.us>  
  
# Install Stash  
ENV STASH_VERSION 3.0.1  
RUN curl -Lks
http://www.atlassian.com/software/stash/downloads/binary/atlassian-
stash-${STASH_VERSION}.tar.gz -o /root/stash.tar.gz  
RUN /usr/sbin/useradd --create-home --home-dir /home/stash --shell /bin/bash
stash  
RUN mkdir /opt/stash  
RUN tar zxf /root/stash.tar.gz --strip=1 -C /opt/stash  
RUN chown -R stash:stash /opt/stash  
  
# Install Stash service  
RUN mkdir /etc/service/stash  
ADD stash.sh /etc/service/stash/run  
  
RUN chmod +x /etc/service/stash/run  
RUN chown root: /etc/service/stash/run  
  
# Launching Stash  
ENV STASH_HOME /home/stash  
EXPOSE 7990 7999  

