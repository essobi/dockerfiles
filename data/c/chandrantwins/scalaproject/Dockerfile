# Pull base image  
FROM selenium/standalone-chrome  
  
# Install OpenJDK and Maven  
RUN sudo apt-get update && \  
sudo apt-get install -y --no-install-recommends \  
curl \  
openjdk-8-jdk-headless \  
maven && \  
sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists  
  
USER root  
  
#  
# php installation  
#  
RUN sudo apt-get update  
RUN sudo apt-get install software-properties-common python-software-properties
-y  
RUN LC_ALL=C.UTF-8 sudo add-apt-repository -y ppa:ondrej/php  
RUN sudo apt-get update  
RUN sudo apt-get install php5.6 -y  
RUN sudo apt-get install php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-xml
php5.6-cli php5.6-imap php5.6-curl -y  
  
#  
# mysql installation  
#  
RUN sudo apt-get update  
RUN apt-get install -y mysql-server-5.7  
RUN service mysql stop  
RUN sed -e 's/^datadir\t.*$/datadir = \/data/' -i /etc/mysql/my.cnf  
RUN sed -e 's/^bind-address\t.*$/bind-address = 0.0.0.0/' -i /etc/mysql/my.cnf  
RUN cp /etc/mysql/my.cnf /usr/share/mysql/my-default.cnf  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN sudo usermod -d /var/lib/mysql/ mysql  
EXPOSE 3306  
CMD mysqld_safe  
  
#  
# Scala and sbt Dockerfile  
#  
# Env variables  
ENV SCALA_VERSION 2.12.4  
ENV SBT_VERSION 1.0.2  
# Scala expects this file  
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release  
  
# Install Scala  
## Piping curl directly in tar  
RUN \  
curl -fsL
https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /root/ && \  
echo >> /root/.bashrc && \  
echo "export PATH=~/scala-$SCALA_VERSION/bin:$PATH" >> /root/.bashrc  
  
# Install sbt  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt && \  
sbt sbtVersion  
  
RUN service mysql start  
  
# Define working directory  
WORKDIR /root  
COPY /test /root  

