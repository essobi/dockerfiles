FROM ubuntu:15.10  
MAINTAINER coders51 <dev@coders51.com>  
  
  
LABEL Description="Ruby 2.2.1 image with xorg and xvfb. Useful to run test
with selenium"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y git vim curl wget links apache2 php5
php5-curl php5-mysql php5-mcrypt php5-gd xvfb firefox  
RUN apt-get install -y openjdk-7-jre-headless xfonts-100dpi xfonts-75dpi
xfonts-scalable xfonts-cyrillic imagemagick  
  
RUN apt-get install -y curl libxml2-dev libxslt-dev libcurl4-openssl-dev
libreadline6-dev libssl-dev patch build-essential zlib1g-dev openssh-server
libyaml-dev libicu-dev libmysqlclient-dev  
  
RUN mkdir /tmp/ruby  
RUN cd /tmp/ruby && curl --silent ftp://ftp.ruby-
lang.org/pub/ruby/2.2/ruby-2.2.1.tar.gz | tar xz  
RUN cd /tmp/ruby/ruby-2.2.1 && ./configure --disable-install-rdoc && make
install  
  
RUN gem install bundler  
  
RUN echo "LC_ALL=\"en_US.UTF-8\"" >> /etc/default/locale  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  

