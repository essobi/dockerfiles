FROM ubuntu  
  
MAINTAINER Cougar <cougar@random.ee>  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://ppa.launchpad.net/arune/auml-atom-daily/ubuntu xenial
main" > /etc/apt/sources.list.d/arune.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6FA6987C  
RUN apt-get update  
RUN apt-get install -y atom  
RUN apt-get clean  
  
RUN mv /etc/atom/atom.conf.template /etc/atom/atom.conf  
RUN sed -iE 's/^\\(ProtocolFile\\)/#&/' /etc/atom/atom.conf  
RUN sed -iE 's/^#\\(ProtocolFile = \/\\)/\1/' /etc/atom/atom.conf  
  
VOLUME [ "/etc/atom" ]  
  
WORKDIR /etc/atom  
  
ENV CANNET udp:192.168.1.250:1100  
EXPOSE 1200  
EXPOSE 1100/udp  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
CMD [ "atomd" ]  

