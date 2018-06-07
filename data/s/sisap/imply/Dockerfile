FROM ubuntu:16.04  
# Modificar per canviar versió  
ENV IMPLY_VERSION 2.4.5  
  
COPY nodesource-pubkey /root/nodesource-pubkey  
  
RUN \  
# Prepare OS  
apt-get update \  
&& apt-get -y install --no-install-recommends curl apt-transport-https
software-properties-common python python2.7 perl \  
# Setup sources for Java, Node  
&& apt-key add /root/nodesource-pubkey \  
&& echo "deb https://deb.nodesource.com/node_4.x "$(lsb_release -c -s)" main"
> /etc/apt/sources.list.d/nodesource.list \  
&& echo "deb-src https://deb.nodesource.com/node_4.x "$(lsb_release -c -s)"
main" >> /etc/apt/sources.list.d/nodesource.list \  
&& add-apt-repository ppa:webupd8team/java -y \  
&& apt-get update \  
# Install Java  
&& (echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections) \  
&& apt-get install -y oracle-java8-installer oracle-java8-set-default \  
# Install Node  
&& apt-get -y install --no-install-recommends nodejs \  
# Install Imply  
&& curl -O https://static.imply.io/release/imply-${IMPLY_VERSION}.tar.gz \  
&& tar -xzf imply-${IMPLY_VERSION}.tar.gz \  
&& mkdir /imply \  
&& mv imply-${IMPLY_VERSION}/* /imply/ \  
# Remove stuff we probably don't need, to save on space  
&& apt-get -y remove software-properties-common \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -fr \  
imply-${IMPLY_VERSION}.tar.gz \  
/var/cache/oracle-jdk8-installer \  
/usr/lib/jvm/java-8-oracle/src.zip \  
/usr/lib/jvm/java-8-oracle/javafx-src.zip \  
/usr/lib/jvm/java-8-oracle/lib/visualvm \  
/usr/lib/jvm/java-8-oracle/lib/missioncontrol  
  
WORKDIR /imply  
CMD ["bin/supervise", "-c", "conf/supervise/quickstart.conf"]  

