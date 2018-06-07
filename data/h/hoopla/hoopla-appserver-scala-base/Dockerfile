# Dockerfile to build hoopla/hoopla-docker-scala-base  
FROM evarga/jenkins-slave  
MAINTAINER Halvor Granskogen Bjørnstad <halvor@hoopla.no>  
  
# Install sbt  
RUN wget https://dl.bintray.com/sbt/debian/sbt-0.13.9.deb && \  
dpkg -i sbt-0.13.9.deb && \  
rm sbt-0.13.9.deb && \  
apt-get update && apt-get install -y sbt  
  
# Install python2.7 and python-pip  
RUN apt-get update && \  
apt-get -y install python2.7 python-pip  
  
# Install wkhtmltopdf 0.12.2.1  
RUN apt-get install -y libxfont1 xfonts-encodings xfonts-utils xfonts-base
xfonts-75dpi && \  
wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb && \  
dpkg -i wkhtmltox-0.12.2.1_linux-trusty-amd64.deb && \  
rm wkhtmltox-0.12.2.1_linux-trusty-amd64.deb  
  
##### #  
# Docker within docker:  
# See https://github.com/ahunnargikar/jenkins-dind/tree/master/single-docker  
##### #  
# General utils:  
RUN apt-get -y install wget curl git jgit-cli  
  
# Install python packages for build scripts.  
RUN pip install sh && \  
pip install logging && \  
pip install setuptools  
  
# Install SWIG, and some python deps.  
RUN apt-get update && \  
apt-get install -y --fix-missing swig libpq-dev python-dev libffi-dev  
  
# Install docker-CLI binary. Version 1.1.2 bc. of newest ubuntu repo version  
ADD https://get.docker.com/builds/Linux/x86_64/docker-1.9.0
/usr/local/bin/docker  
RUN chmod +x /usr/local/bin/docker  
  
# install diff-pdf  
RUN wget -q -O - http://archive.getdeb.net/getdeb-archive.key | sudo apt-key
add - && \  
sh -c 'echo "deb http://archive.getdeb.net/ubuntu trusty-getdeb apps" >>
/etc/apt/sources.list.d/getdeb.list' && \  
apt-get update && \  
apt-get install -y diff-pdf  
  
RUN chmod u+w /etc/sudoers && \  
echo "%jenkins ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
chmod u-w /etc/sudoers && \  
visudo --check  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

