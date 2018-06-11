FROM ubuntu:14.04  
MAINTAINER Yugesh A "yugesh.a@tcs.com"  
RUN sudo apt-get update -y && sudo apt-get upgrade --fix-missing -y && \  
sudo apt-get install software-properties-common curl -y && \  
sudo add-apt-repository ppa:webupd8team/java && \  
sudo apt-get update -y  
  
# JDK INSTALLATION STARTS  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections && \  
sudo apt-get install oracle-java8-set-default oracle-java8-installer -y && \  
sudo apt-get install -f && \  
sudo dpkg --configure -a  
  
# JDK INSTALLATION ENDS  
# TOMCAT INSTALLATION STARTS  
ENV CATALINA_HOME /usr/local/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS  
RUN set -ex \  
&& for key in \  
05AB33110949707C93A279E3D3EFE6B686867BA6 \  
07E48665A34DCAFAE522E5E6266191C37C037D42 \  
47309207D818FFD8DCD3F83F1931D684307A10A5 \  
541FBE7D8F78B25E055DDEE13C370389288584E7 \  
61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \  
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
9BA44C2621385CB966EBA586F72C284D731FABEE \  
A27677289986DB50844682F8ACB77FC2E86E29AC \  
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.33  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
ADD tomcat-users.xml /opt/tomcat/conf/  
  
# TOMCAT INSTALLATION ENDS  
# POSTGRES INSTALLATION STARTS  
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
EXPOSE 8009 8080 9990 5432  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
#CMD["catalina.sh","run"]  
CMD ["/usr/lib/postgresql/9.4/bin/postgres", "-D",
"/var/lib/postgresql/9.4/main", "-c",
"config_file=/etc/postgresql/9.4/main/postgresql.conf"]  

