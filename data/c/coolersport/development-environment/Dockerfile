FROM consol/ubuntu-xfce-vnc  
  
USER root  
  
RUN apt-get update && \  
apt-get install software-properties-common -y && add-apt-repository
ppa:webupd8team/java && \  
apt-get update -y && apt-get upgrade -y && \  
# install jdk 8  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get install oracle-java8-installer -y && \  
update-java-alternatives -s java-8-oracle && \  
apt-get install oracle-java8-set-default -y && \  
# install git  
apt-get install git -y && \  
# install maven 3.2.5  
wget https://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.tar.gz -O /tmp/maven.tar.gz && \  
cd /usr/local && \  
tar -xzf /tmp/maven.tar.gz && \  
ln -s /usr/local/apache-maven-3.2.5/bin/mvn /usr/local/bin/mvn && \  
# install ssh  
apt-get install openssh-server -y && \  
mkdir /var/run/sshd && \  
#sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g'
/etc/ssh/sshd_config && \  
# install gosu  
apt-get install -y \--no-install-recommends ca-certificates wget && \  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \  
wget "https://github.com/tianon/gosu/releases/download/1.10/gosu-$dpkgArch" -O
/usr/local/bin/gosu && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true && \  
# complete gosu  
apt-get autoremove -y  
  
EXPOSE 22  
USER 1984  
  
#ENTRYPOINT []  
#CMD ["/usr/sbin/sshd", "-D"]  

