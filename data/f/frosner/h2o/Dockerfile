# pull base image  
FROM ubuntu:14.04  
  
RUN \  
echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb ||
true";};' | tee /etc/apt/apt.conf.d/no-cache && \  
echo "deb http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu trusty main
universe" >> /etc/apt/sources.list && \  
apt-get update -q -y && \  
apt-get dist-upgrade -y && \  
apt-get clean && \  
rm -rf /var/cache/apt/*  
  
# Install Oracle Java 7  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget unzip python-pip
python-sklearn python-pandas python-numpy python-matplotlib software-
properties-common python-software-properties && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update -q && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java7-installer && \  
apt-get clean  
  
# Fetch h2o latest_stable  
RUN \  
wget http://h2o-release.s3.amazonaws.com/h2o/latest_stable -O latest && \  
wget --no-check-certificate -i latest -O /opt/h2o.zip && \  
unzip -d /opt /opt/h2o.zip && \  
rm /opt/h2o.zip && \  
cd /opt && \  
cd `find . -name 'h2o.jar' | sed 's/.\///;s/\/h2o.jar//g'` && \  
cp h2o.jar /opt && \  
/usr/bin/pip install `find . -name "*.whl"` && \  
wget
https://raw.githubusercontent.com/h2oai/h2o-3/master/docker/start-h2o-docker.sh  
  
RUN mkdir /data  
VOLUME /data  
WORKDIR /data  
  
EXPOSE 54321  
EXPOSE 54322  
  
ADD entrypoint /entrypoint  
  
ENTRYPOINT ["/entrypoint"]  

