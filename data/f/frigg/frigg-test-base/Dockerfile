FROM phusion/baseimage:0.9.17  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV HOME /root  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update && \  
apt-get install -y build-essential software-properties-common libssl-dev && \  
apt-get install -y byobu curl libcurl4-gnutls-dev git unzip vim wget
libxml2-dev libxslt-dev  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get update && \  
apt-get install -y libjpeg62 libjpeg62-dev zlib1g-dev graphicsmagick
imagemagick  
  
RUN apt-get update && apt-get install -y ca-certificates wget  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" >>
/etc/apt/sources.list  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add -  
RUN apt-get update && apt-get install -y postgresql-9.4 postgresql-server-
dev-9.4  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/;
rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R
0700 /etc/ssl/private; chown -R postgres /etc/ssl/private  
RUN service postgresql start && su - postgres -c "createuser -s root" &&
service postgresql stop  
COPY files/pg_hba.conf /etc/postgresql/9.4/main/pg_hba.conf  
  
# Apache  
RUN apt-get update && apt-get install -y apache2 libapache2-mod-wsgi
libapache2-mod-xsendfile ssl-cert poppler-utils  
  
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" >>
/etc/apt/sources.list && \  
curl https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | \  
apt-key add - && \  
apt-get update && apt-get install -y rabbitmq-server  
  
RUN apt-get update && apt-get install -y redis-server mysql-server mongodb
memcached libmysqlclient-dev  
RUN apt-get update && apt-get install -y libffi6 libffi-dev  
RUN apt-get update && apt-get install -y python python-dev python-pip python3
python3-dev python3-pip supervisor libboost-python-dev  
  
RUN apt-get update && apt-get install libbz2-dev libsqlite3-dev && wget
https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz && tar -xvf
Python-3.5.0.tgz && cd Python-3.5.0 && ./configure && make && make install  
  
RUN pip install -U pip  
RUN pip3 install -U pip  
RUN pip3 install -U tox virtualenv  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN apt-get update && apt-get install -y maven  
  
# Ruby and jekyll  
RUN apt-get update && apt-get install -y ruby ruby-dev ruby-bundler python-
software-properties && apt-add-repository ppa:brightbox/ruby-ng && apt-get
update && apt-get install -y ruby2.2 ruby2.2-dev ruby-switch && ruby-switch
--set ruby2.2 && gem install jekyll rake html-proofer  
  
# Nodejs  
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && apt-get install nodejs -y  
  
RUN wget https://storage.googleapis.com/golang/go1.5.linux-amd64.tar.gz  
RUN tar -C /usr/local -xzf go1.5.linux-amd64.tar.gz  
ENV GOROOT /usr/local/go  
ENV GOPATH /usr/local/gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
# Sbt  
RUN wget https://dl.bintray.com/sbt/debian/sbt-0.13.6.deb && dpkg -i
sbt-0.13.6.deb  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

