FROM library/ruby:2.3.1  
MAINTAINER Yoann Vanitou <yvanitou@gmail.com>  
  
# Déclaration des variables d'envoronement  
ENV PORTUS_VERSION 2.2.0  
ENV COMPOSE 1  
ENV RAILS_ENV production  
  
# Téléchargement du package  
ADD https://github.com/SUSE/Portus/archive/$PORTUS_VERSION.tar.gz
/tmp/portus.tar.gz  
  
# Installation du package  
RUN cd /tmp \  
&& tar -zxvf /tmp/portus.tar.gz \  
&& rm -v /tmp/portus.tar.gz \  
&& mv -v /tmp/Portus-2.2.0/ /portus  
  
# Build  
RUN cd /portus && bundle install --retry=3 && bundle binstubs phantomjs  
RUN apt-get update && \  
apt-get install -y --no-install-recommends nodejs  
  
# Expose le port  
EXPOSE 3000/tcp  
  
# Répertoire par défaut  
WORKDIR /portus  
  
# Execute le programme  
CMD ["puma", "-b", "tcp://0.0.0.0:3000", "-w", "3"]  

