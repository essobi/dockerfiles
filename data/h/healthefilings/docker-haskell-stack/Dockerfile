FROM buildpack-deps:trusty  
MAINTAINER Oscar Rocha <orocha@healthefilings.com>  
  
# Versions to install.  
ENV STACK_VERSION 1.5.0  
ENV RUBY_BASE_VERSION 2.3  
ENV RUBY_VERSION 2.3.1  
ENV PG_CLIENT_VERSION 9.5  
# ENV variables required to build the image.  
ENV STACK_DOWNLOAD_URL
https://github.com/commercialhaskell/stack/releases/download/v$STACK_VERSION/stack-$STACK_VERSION-
linux-x86_64.tar.gz  
ENV DEBIAN_FRONTEND noninteractive  
ENV PATH $PATH:/root/.local/bin  
ENV LANG C.UTF-8  
RUN gpg --keyserver pgpkeys.mit.edu --recv-key 010908312D230C5F  
RUN gpg -a --export 010908312D230C5F | sudo apt-key add -  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \  
sudo apt-key add -  
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg
main" >> /etc/apt/sources.list.d/postgresql.list'  
  
RUN apt-get update -q && \  
apt-get install -qy libgmp-dev git-core curl zlib1g-dev build-essential \  
libssl-dev libreadline-dev libyaml-dev libxml2-dev libxslt1-dev \  
libcurl4-openssl-dev python-software-properties libffi-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install stack  
RUN mkdir -p /root/.local/bin && \  
curl -L $STACK_DOWNLOAD_URL | tar zx -C /root/.local/bin/ --wildcards
'*/stack' \--strip=1 && \  
chmod +x /root/.local/bin/stack  
RUN stack setup  
  
# Install Ruby  
RUN echo "deb http://ftp.debian.org/debian wheezy main" >>
/etc/apt/sources.list  
RUN apt-get update  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
RUN cd  
RUN wget http://ftp.ruby-
lang.org/pub/ruby/$RUBY_BASE_VERSION/ruby-$RUBY_VERSION.tar.gz  
RUN tar -xzvf ruby-$RUBY_VERSION.tar.gz  
RUN cd ruby-$RUBY_VERSION/ && ./configure && make && sudo make install  
RUN gem install bundler  
RUN npm -g install bower  
  
# Install PG Client  
RUN apt-get -y install postgresql-client-$PG_CLIENT_VERSION  

