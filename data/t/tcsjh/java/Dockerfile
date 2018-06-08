############################################################  
# TCSJOHNHUXLEY GFL Server Java Base Image #  
############################################################  
  
#Image properties  
FROM tcsjh/base:2.1  
  
#Install packages  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
DA1A4A13543B466853BAF164EB9B1D8886F44E2A && \  
echo "deb http://ppa.launchpad.net/openjdk-r/ppa/ubuntu trusty main" >>
/etc/apt/sources.list && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
openjdk-8-jre-headless \  
jsvc && \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  

