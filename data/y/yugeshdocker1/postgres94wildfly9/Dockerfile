FROM ubuntu:14.04  
MAINTAINER Yugesh A "yugesha@gmail.com"  
RUN sudo apt-get update -y && sudo apt-get upgrade --fix-missing -y && \  
sudo apt-get install software-properties-common -y && \  
sudo add-apt-repository ppa:webupd8team/java && \  
sudo apt-get update -y  
  
# JDK INSTALLATION STARTS  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections && \  
sudo apt-get install oracle-java8-set-default oracle-java8-installer -y && \  
sudo apt-get install -f && \  
sudo dpkg --configure -a  
  
# JDK INSTALLATION ENDS  
# WILDFLY INSTALLATION STARTS  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 9.0.1.Final  
  
# Add the WildFly distribution to /opt  
RUN cd /opt && wget
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz  
RUN cd /opt && tar xvf wildfly-$WILDFLY_VERSION.tar.gz && rm
wildfly-$WILDFLY_VERSION.tar.gz  
  
# Make sure the distribution is available from a well-known place  
RUN ln -s /opt/wildfly-$WILDFLY_VERSION /opt/wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/wildfly  
  
# WILDFLY INSTALLATION ENDS  
# POSTGRESQL INSTALLATION STARTS  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-
keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
RUN sudo echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main"
> /etc/apt/sources.list.d/pgdg.list  
  
# Install ``python-software-properties``, ``software-properties-common`` and
PostgreSQL 9.4  
# There are some warnings (in red) that show up during the build. You can hide  
# them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive  
RUN sudo apt-get update -y && \  
apt-get install -y software-properties-common postgresql-9.4 postgresql-
client-9.4 postgresql-contrib-9.4 && \  
sudo apt-get update -y  
  
# Note: The official Debian and Ubuntu images automatically ``apt-get clean``  
# after each ``apt-get``  
# RUN groupadd -r postgres -g 533 && \  
# useradd -u 531 -r -g postgres -d /opt/postgres -s /bin/false -c "Postgres  
# user" postgres -p postgres && \  
RUN sudo adduser postgres sudo  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
# POSTGRESQL INSTALLATION ENDS  
# Expose the ports we're interested in  
EXPOSE 8080 9990 5432  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
# CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement",
"0.0.0.0"]  
CMD ["/usr/lib/postgresql/9.4/bin/postgres", "-D",
"/var/lib/postgresql/9.4/main", "-c",
"config_file=/etc/postgresql/9.4/main/postgresql.conf"]  

