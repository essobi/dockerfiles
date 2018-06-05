FROM ubuntu:14.04  
MAINTAINER Ender TUNC < araknafobiatr@gmail.com >  
  
# Set locales  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LC_CTYPE en_GB.UTF-8  
# Fix sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install dependencies  
ENV ACTIVATOR_VERSION 1.3.9  
RUN apt-get update && \  
apt-get install -y git build-essential curl wget zip unzip software-
properties-common  
  
RUN sudo add-apt-repository -y ppa:ondrej/mysql-5.7 \  
&& apt-get update \  
&& apt-get install -y debconf-utils \  
&& echo mysql-server-5.7 mysql-server/root_password password .not | debconf-
set-selections \  
&& echo mysql-server-5.7 mysql-server/root_password_again password .not |
debconf-set-selections \  
&& apt-get install -y mysql-server-5.7 -o pkg::Options::="--force-confdef" -o
pkg::Options::="--force-confold" \--fix-missing \  
&& apt-get install -y net-tools --fix-missing  
  
RUN echo "service mysql start" >> /etc/bash.bashrc  
RUN echo "mysql --user=root --password=.not --execute='CREATE DATABASE
hunger1'" >> /etc/bash.bashrc  
RUN /bin/bash -c "/usr/bin/mysqld_safe &" && \  
sleep 5 && \  
mysql --user=root --password=.not --execute="CREATE DATABASE hunger"  
  
# Install Java and dependencies  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer wget unzip tar && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $PATH:/opt/activator/bin  
  
# Install play  
RUN wget http://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VERSION}/typesafe-activator-${ACTIVATOR_VERSION}.zip &&
\  
unzip typesafe-activator-${ACTIVATOR_VERSION}.zip && \  
mv activator-dist-${ACTIVATOR_VERSION} /opt/activator && \  
chown -R root:root /opt/activator && \  
rm typesafe-activator-${ACTIVATOR_VERSION}.zip  
  
# Expose Code volume and play ports 9000 default 9999 debug 8888 activator ui  
VOLUME "/var/lib/mysql"  
  
EXPOSE 9000  
EXPOSE 9999  
EXPOSE 8888  
EXPOSE 3306  
CMD ["/bin/bash"]  

