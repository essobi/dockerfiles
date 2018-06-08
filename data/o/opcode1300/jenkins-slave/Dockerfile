FROM evarga/jenkins-slave  
  
MAINTAINER Alex Newman<alex@opcode1300.com>  
  
USER root  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
E1DD270288B4E6030699E45FA1715D88E1DF1F24 &&\  
echo 'deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main' >
/etc/apt/sources.list.d/git.list &&\  
apt-get -q update &&\  
DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends git curl &&\  
apt-get -q autoremove &&\  
apt-get -q clean -y &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /var/cache/apt/*.bin &&\  
/var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
USER jenkins  

