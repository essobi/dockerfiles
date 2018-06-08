# Jenkins server with some usual additional tools  
FROM jenkins  
MAINTAINER Frédéric Peignot frederic.peignot@free.fr  
  
ENV MAINTAINER "Frédéric Peignot"  
USER root  
  
# Install packages  
RUN apt-get update \  
&& apt-get install -y apt-utils  
  
RUN apt-get install -y doxygen \  
&& apt-get install -y php5 \  
&& apt-get install -y phpunit \  
&& apt-get install -y graphviz \  
&& apt-get install -y ruby-full \  
&& apt-get install -y rake \  
&& apt-get install -y iceweasel \  
&& apt-get install -y mysql-client  
  
# Install ruby gems  
RUN gem install minitest  
RUN gem install minitest-ci  
RUN gem install dbi  
  
# in order to install native ruby gems a development environment is required  
RUN apt-get install -y build-essential bison openssl libreadline6
libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev
libxml2-dev autoconf libc6-dev ncurses-dev automake libtool  
RUN gem install compass  
RUN gem install watir-webdriver  
RUN gem install headless  
  
# Install packages for debug  
RUN apt-get install -y vim && apt-get install -y sudo  
  
# PHP static analyzers  
ADD bin/* /usr/local/bin/  
ADD php/* /usr/local/share/php/  
  
RUN wget
https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz  
RUN tar xvf geckodriver-v0.11.1-linux64.tar.gz  
RUN mv geckodriver /usr/local/bin  
  
# drop back to the regular jenkins user - good practice  
USER jenkins  
  
# Install jenkins plugins  
COPY plugins.txt /plugins.txt  
RUN /usr/local/bin/plugins.sh /plugins.txt  
  
# following line is only used for testing, to be removed  
USER root  
  

