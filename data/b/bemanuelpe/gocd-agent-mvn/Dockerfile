FROM gocd/gocd-agent  
  
MAINTAINER Bruno Emanuel <bemanuel.pe@gmail.com>  
  
ENV MVN_VER=apache-maven-3.3.9  
ENV MVN_FILE=${MVN_VER}-bin.tar.gz  
ENV
MVN_URL=http://mirror.nbtelecom.com.br/apache/maven/maven-3/3.3.9/binaries/${MVN_FILE}
\  
DEBIAN_FRONTEND="noninteractive"  
  
COPY spotify /tmp/spotify  
  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | sudo
tee /etc/apt/sources.list.d/docker.list && \  
apt-key adv \--keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
apt-get update && \  
apt-get -y install wget openjdk-7-jdk docker-engine=1.10.3-0~trusty && \  
apt-get clean && \  
echo "Instalação do Maven em /usr/local/mvn" && \  
wget -t0 -c -P /tmp/ ${MVN_URL} && \  
rm -rf /var/run/cache/apt/* && \  
tar xf /tmp/${MVN_FILE} -C /usr/local/ && \  
mv /usr/local/${MVN_VER} /usr/local/mvn && \  
rm /tmp/${MVN_FILE} && \  
echo "Preparação do Repository do Componente Docker - MVN" && \  
mkdir -p ~go/.m2/repository/com ~/.m2/repository/com && \  
cp -r /tmp/spotify ~/.m2/repository/com/. && \  
cp -r /tmp/spotify ~go/.m2/repository/com/.  
  
RUN echo "Alterações do usuário" && \  
chown go. -R ~go/.m2 && \  
groupmod -g 1101 docker && \  
adduser go docker  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

