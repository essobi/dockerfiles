FROM previousnext/base:latest  
MAINTAINER nick_schuch  
  
##  
# Base.  
##  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y build-essential  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y byobu curl git htop man unzip vim wget  
RUN apt-get install -y python-software-properties  
RUN rm -rf /var/lib/apt/lists/*  
  
##  
# Ruby.  
##  
RUN apt-add-repository ppa:brightbox/ruby-ng-experimental  
RUN apt-get update  
RUN apt-get install -y ruby2.0 ruby2.0-dev ruby2.0-doc  
RUN rm -rf /var/lib/apt/lists/*  
  
##  
# Serverspec.  
##  
RUN gem install bundler -v 1.6.3  
RUN gem install rake  
  
##  
# Travis.  
##  
RUN gem install travis --no-rdoc --no-ri  
RUN mkdir /root/.travis  
RUN git clone https://github.com/travis-ci/travis-build.git
/root/.travis/travis-build && cd /root/.travis/travis-build && git reset
--hard e5553110116f026075d47dfd922c5b7427539dc7  
RUN travis version  
  
##  
# Supervisord.  
##  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
VOLUME ["/data"]  
WORKDIR /data  
CMD ["/root/start.sh"]  

