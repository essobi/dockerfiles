FROM ubuntu:trusty  
  
RUN apt-get update  
RUN apt-get -y install software-properties-common curl  
  
# Install gosu  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& curl -L -o /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& curl -L -o /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# Install java  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java8-installer oracle-java8-set-default #ant  
  
# Install PDI  
RUN mkdir /usr/src/app  
WORKDIR /usr/src/app  
RUN curl -L
http://downloads.sourceforge.net/project/pentaho/Data%20Integration/4.2.1-stable/pdi-
ce-4.2.1-stable.tar.gz | tar xz --strip-components=1  
  
# Install newer MySQL connector  
RUN rm libext/JDBC/mysql-connector-java-5.1.17.jar \  
&& curl -L https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.35.tar.gz | tar xz --strip-components=1 -C libext/JDBC/ mysql-
connector-java-5.1.35/mysql-connector-java-5.1.35-bin.jar  
  
ENV PATH=/usr/src/app:$PATH  
  
COPY with_app_user /  
COPY configure_and_start /  
ENTRYPOINT ["/with_app_user", "/configure_and_start"]  

