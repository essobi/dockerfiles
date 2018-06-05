# container for building java8 and erlang/elixir apps  
  
FROM ubuntu:xenial  
MAINTAINER talentdeficit  
  
ENV DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true  
  
RUN locale-gen --purge en_US.UTF-8 \  
&& dpkg-reconfigure locales  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# install openjdk8, git, tar, zip, unzip, ca certs, openssh, build-essential,
python, pip...  
RUN apt-get update -qqy \  
&& apt-get upgrade -qqy \  
&& apt-get -qqy --no-install-recommends install \  
openssh-client ssh-askpass\  
apt-transport-https ca-certificates \  
openjdk-8-jdk \  
tar zip unzip \  
wget curl \  
git \  
build-essential \  
less nano tree \  
python python-pip groff \  
&& rm -rf /var/lib/apt/lists/*  
# set java env variables  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV JAVA_OPTS -Xmx2G -Xms2G -XX:PermSize=256M -XX:MaxPermSize=256m  
  
# install erlang and elixir  
RUN wget -q -P /tmp https://packages.erlang-solutions.com/erlang-
solutions_1.0_all.deb \  
&& dpkg -i /tmp/erlang-solutions_1.0_all.deb \  
&& apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
erlang=1:19.1-1 \  
elixir=1.3.3-1  

