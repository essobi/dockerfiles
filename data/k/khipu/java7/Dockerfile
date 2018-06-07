FROM khipu/base-apps:latest  
MAINTAINER developers@khipu.com  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >
/etc/apt/sources.list.d/webupd8team-java-trusty.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install ca-certificates-java oracle-java7-installer oracle-java7-set-
default -y && \  
dpkg-reconfigure oracle-java7-installer # creates link to
/etc/ssl/certs/java/cacerts  
# jvm fixes  
RUN curl -sSL
https://s3.amazonaws.com/downloads.khipu.com/jvm/tzdata2016d/zi/Santiago -o
/usr/lib/jvm/java-7-oracle/jre/lib/zi/America/Santiago \  
&& sed -i 's/.*networkaddress.cache.ttl=.*/networkaddress.cache.ttl=5/g'
/usr/lib/jvm/java-7-oracle/jre/lib/security/java.security \  
&& sed -i
's/.*networkaddress.cache.negative.ttl=.*/networkaddress.cache.negative.ttl=5/g'
/usr/lib/jvm/java-7-oracle/jre/lib/security/java.security  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/bin/true"]  

