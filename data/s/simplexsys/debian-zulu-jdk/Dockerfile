FROM simplexsys/debian-cli-powered  
MAINTAINER qsys <kurt.sys@gmail.com>  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
0x219BD9C9 &&\  
echo "deb http://repos.azulsystems.com/debian stable main" >>
/etc/apt/sources.list.d/zulu.list &&\  
apt-get -qq update &&\  
apt-get -y install zulu-8=8.7.0.5  

