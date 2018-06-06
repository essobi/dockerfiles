FROM kalilinux/kali-linux-docker  
MAINTAINER Ralph May <ralph@thedarkcloud.net>  
  
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >>
/etc/apt/sources.list  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | \  
debconf-set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | \  
debconf-set-selections  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
oracle-java8-installer \  
ca-certificates \  
openssh-server \  
expect \  
curl && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\  
update-java-alternatives -s java-8-oracle  
  
WORKDIR /opt  
RUN mkdir /opt/cobaltstrike  
COPY ./docker-entrypoint.sh /opt/  
COPY ./cloudfront.sh /opt/cobaltstrike/  
COPY ./key.sh /opt/cobaltstrike/  
RUN chmod +x /opt/docker-entrypoint.sh  
RUN chmod +x /opt/cobaltstrike/key.sh  
RUN chmod +x /opt/cobaltstrike/cloudfront.sh  
  
WORKDIR /opt/cobaltstrike  
RUN mkdir /opt/cobaltstrike/profiles  
COPY ./profiles/*.profile /opt/cobaltstrike/profiles/  
  
EXPOSE 50050  
EXPOSE 22  
ENTRYPOINT ["/opt/docker-entrypoint.sh"]  

