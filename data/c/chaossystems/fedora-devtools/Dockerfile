FROM fedora:27  
MAINTAINER Greg Orzell <chaos@chaossystems.io>  
  
ARG SCALA_VERSION=2.12.4  
# Base Packages  
RUN dnf makecache && \  
dnf install -y \  
# Tools  
curl \  
fish \  
fzf \  
go \  
hostname \  
make \  
sudo \  
the_silver_searcher \  
tmux \  
traceroute \  
vim \  
wget \  
# Development tools sbt  
git \  
java-9-openjdk-devel \  
python \  
python-pip \  
ruby  
  
# Node  
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - &&
\  
yum -y install nodejs  
  
# Scala Tools  
RUN curl -Lso /etc/yum.repos.d/bintray-sbt-rpm.repo
https://bintray.com/sbt/rpm/rpm && \  
curl -LsO
https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.rpm
&& \  
dnf install -y \  
sbt \  
scala-$SCALA_VERSION.rpm && \  
sbt update && \  
curl -Lso /usr/local/bin/amm
https://github.com/lihaoyi/Ammonite/releases/download/1.0.5/2.12-1.0.5 && \  
chmod +x /usr/local/bin/amm && \  
dnf clean all  
  
CMD ["/usr/bin/tmux"]  

