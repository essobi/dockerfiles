# Dockerfile BareOS storage daemon  
FROM debian:stretch  
MAINTAINER Brightside <sweetdimensions@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -y install curl software-properties-common gnupg
wget  
  
RUN curl -Ls
http://download.bareos.org/bareos/release/latest/Debian_9.0/Release.key | apt-
key --keyring /etc/apt/trusted.gpg.d/bareos-keyring.gpg add - && \  
curl -Ls http://download.bareos.org/bareos/contrib/Debian_9.0/Release.key |
apt-key --keyring /etc/apt/trusted.gpg.d/bareos-keyring.gpg add - && \  
echo 'deb http://download.bareos.org/bareos/release/latest/Debian_9.0/ /' >
/etc/apt/sources.list.d/bareos.list && \  
echo 'deb http://download.bareos.org/bareos/contrib/Debian_9.0/ /' >>
/etc/apt/sources.list.d/bareos.list && \  
apt-get update -qq && \  
apt-get install -qq -y bareos-storage curl && \  
apt-get clean  
  
COPY docker-entrypoint.sh /  
RUN chmod u+x /docker-entrypoint.sh  
RUN tar cfvz /bareos-sd.tgz /etc/bareos/bareos-sd.d  
  
EXPOSE 9103  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/usr/sbin/bareos-sd", "-u", "bareos", "-f"]  

