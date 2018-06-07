FROM ubuntu:16.04  
MAINTAINER Alexey Zhokhov <alexey@zhokhov.com>  
  
# Update apt-get  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
apt-transport-https \  
ssh \  
net-tools \  
openvpn \  
software-properties-common \  
procps \  
dnsutils \  
unzip \  
zip \  
uchardet \  
git \  
redis-server \  
nano \  
curl \  
wget \  
httpie \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && apt-get upgrade -y && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# postgresql  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >>
/etc/apt/sources.list.d/pgdg.list  
RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
  
# Update apt-get  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
postgresql-client-10 \  
postgresql-10 \  
postgresql-contrib-10 \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
ENV PATH $PATH:/usr/lib/postgresql/$PG_MAJOR/bin  
ENV POSTGRES_HOME /usr/lib/postgresql/10/  
ENV PG_MAJOR 10  
ENV PGDATA /var/lib/postgresql/data  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN locale-gen en_US.UTF-8  
  
ADD locale.sh /  
RUN chmod a+x /locale.sh  
RUN /locale.sh  
  
# make the sample config easier to munge (and "correct by default")  
RUN mv -v "/usr/share/postgresql/$PG_MAJOR/postgresql.conf.sample"
/usr/share/postgresql/ \  
&& ln -sv ../postgresql.conf.sample "/usr/share/postgresql/$PG_MAJOR/" \  
&& sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/share/postgresql/postgresql.conf.sample  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres:postgres
/var/run/postgresql && chmod 2777 /var/run/postgresql  
RUN mkdir -p "$PGDATA" && chown -R postgres:postgres "$PGDATA" && chmod 777
"$PGDATA" # this 777 will be replaced by 700 at runtime (allows semi-arbitrary
"--user" values)  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "local all all trust" > /etc/postgresql/$PG_MAJOR/main/pg_hba.conf  
RUN echo "host all all 127.0.0.1/32 trust" >>
/etc/postgresql/$PG_MAJOR/main/pg_hba.conf  
RUN echo "host all all ::1/128 trust" >>
/etc/postgresql/$PG_MAJOR/main/pg_hba.conf  
RUN echo "host all all 0.0.0.0/0 md5" >>
/etc/postgresql/$PG_MAJOR/main/pg_hba.conf  
  
COPY postgresql.conf /etc/postgresql/$PG_MAJOR/main/  
  
# rabbitmq  
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" >>
/etc/apt/sources.list.d/rabbitmq.list  
RUN curl https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key
add -  
  
# Update apt-get  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
rabbitmq-server \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
RUN rabbitmq-plugins enable \--offline rabbitmq_federation  
RUN rabbitmq-plugins enable \--offline rabbitmq_federation_management  
RUN rabbitmq-plugins enable \--offline rabbitmq_shovel  
RUN rabbitmq-plugins enable \--offline rabbitmq_shovel_management  
  
# mongodb  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6  
RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.4 multiverse" >> /etc/apt/sources.list.d/mongodb-
org-3.4.list  
  
# Update apt-get  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y \  
mongodb-org \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
RUN cd /etc/init.d && wget
https://raw.githubusercontent.com/mongodb/mongo/master/debian/init.d -O mongod
&& chmod a+x mongod  
  
# docker  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
RUN apt-key fingerprint 0EBFCD88  
RUN add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable"  
  
# Update apt-get  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y \  
docker-ce \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
# kubectl  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
RUN chmod +x ./kubectl  
RUN mv ./kubectl /usr/local/bin/kubectl  
  
# sdkman  
RUN curl -s "https://get.sdkman.io" | bash  
  
# groovy  
RUN bash -c "source $HOME/.sdkman/bin/sdkman-init.sh && sdk install groovy"  
  
COPY docker-entrypoint.sh /  
RUN chmod a+x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["tail", "-f", "/dev/null"]  

