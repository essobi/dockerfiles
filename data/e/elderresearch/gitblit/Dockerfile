# Basics  
#  
from ubuntu:latest  
maintainer James Moger <james.moger@gitblit.com>  
run apt-get update  
run apt-get install -q -y git-core redis-server  
  
# Install Java 7  
run DEBIAN_FRONTEND=noninteractive apt-get install -q -y software-properties-
common  
run DEBIAN_FRONTEND=noninteractive apt-get install -q -y python-software-
properties  
run DEBIAN_FRONTEND=noninteractive apt-add-repository ppa:webupd8team/java -y  
run apt-get update  
run echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
run DEBIAN_FRONTEND=noninteractive apt-get install oracle-java7-installer -y  
  
# Install Gitblit  
run apt-get install -q -y curl  
run curl -Lks http://dl.bintray.com/gitblit/releases/gitblit-1.6.2.tar.gz -o
/root/gitblit.tar.gz  
run mkdir -p /opt/gitblit  
run tar zxf /root/gitblit.tar.gz -C /opt/gitblit  
run rm -f /root/gitblit.tar.gz  
  
run mkdir -p /opt/gitblit-data  
  
# Setup the Docker container environment and run Gitblit  
VOLUME /opt/gitblit-data  
workdir /opt/gitblit  
copy run.sh /bin/  
run chmod 755 /bin/run.sh  
expose 80  
expose 9418  
expose 29418  
cmd ["/bin/run.sh"]  

