FROM ubuntu  
MAINTAINER Tomas Markauskas <tomas@markauskas.lt>  
  
RUN apt-get update \  
&& apt-get install -y \  
build-essential libffi-dev libgdbm-dev libncurses5-dev libreadline-dev \  
libssl-dev libyaml-dev zlib1g-dev libxml2 libxml2-dev libxslt-dev curl wget  
RUN curl -L -o /tmp/ruby-build.tar.gz \  
https://github.com/sstephenson/ruby-build/archive/master.tar.gz \  
&& cd /tmp \  
&& tar -xvzf ruby-build.tar.gz \  
&& cd ruby-build-master \  
&& ./install.sh \  
&& ruby-build 1.8.7-p370 /opt/ruby-1.8.7-p370  
  
ENV PATH /opt/ruby-1.8.7-p370/bin:$PATH  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
  
CMD [ "irb" ]  

