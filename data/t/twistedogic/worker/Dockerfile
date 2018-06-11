# runnable base  
FROM ubuntu:trusty  
  
# REPOS  
RUN apt-get -y update  
RUN apt-get install -y -q python-software-properties software-properties-
common  
#RUN add-apt-repository -y ppa:gophers/go  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | tee /etc/apt/sources.list.d/10gen.list  
RUN apt-get -y update  
  
#SHIMS  
ENV DEBIAN_FRONTEND noninteractive  
  
# EDITORS  
RUN apt-get install -y -q vim  
RUN apt-get install -y -q nano  
  
# TOOLS  
RUN apt-get install -y -q curl git make wget supervisor unzip  
  
# BUILD  
RUN apt-get install -y -q build-essential g++  
  
# LANGS  
## GO  
RUN apt-get install -y -q golang  
  
## RUBY  
RUN apt-get install -y -q ruby  
  
## NODE  
RUN apt-get install -y -q nodejs  
  
## PHP  
RUN apt-get install -y -q php5  
RUN apt-get install -y -q php-pear  
  
## ERLANG  
RUN apt-get install -y -q erlang  
  
## PYTHON  
RUN apt-get install -y -q python-software-properties  
RUN apt-get install -y -q python  
RUN apt-get install -y -q python-dev  
RUN apt-get install -y -q python-distribute  
RUN apt-get install -y -q python-pip  
RUN pip --no-input --exists-action=w install --upgrade pip  
  
# # # JAVA  
# # # Broken  
RUN apt-get install -y openjdk-7-jre-headless openjdk-6-jre  
  
# LIB  
RUN apt-get install libcurl4-openssl-dev -y  
RUN apt-get install libxml2-dev -y  
RUN apt-get install libglpk-dev -y  
  
RUN wget http://www.scala-lang.org/files/archive/scala-2.11.2.deb && dpkg -i
scala-2.11.2.deb  
RUN apt-get update -y  
RUN apt-get install scala -y  
RUN wget http://dl.bintray.com/sbt/debian/sbt-0.13.5.deb && dpkg -i
sbt-0.13.5.deb  
RUN apt-get update -y  
RUN apt-get install sbt -y  
  
ENV DEBIAN_FRONTEND dialog  
  
RUN \  
echo "# Install OpenSSH Server" ;\  
apt-get -q -y install openssh-server ;\  
mkdir -p /var/run/sshd ;\  
echo 'root:passw0rd' | chpasswd ;\  
\  
true  
  
ADD sshd_config /etc/ssh/sshd_config  
RUN cd /home/ && npm install codebox@0.7.6  
ADD package.json /home/node_modules/codebox/node_modules/connect-gzip-
static/package.json  
RUN cd /home/node_modules/codebox/node_modules/connect-gzip-static/ && npm
install  
RUN mkdir -p /home/myworkspace  
  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  

