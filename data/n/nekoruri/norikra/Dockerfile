FROM ubuntu:trusty  
  
MAINTAINER NAKAYAMA Masahiro <aki@nekoruri.jp>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV JRUBY_VERSION 1.7.17  
ENV PATH /jruby-$JRUBY_VERSION/bin:$PATH  
  
# build norikra and clean  
RUN apt-get update && apt-get -y install build-essential curl git
openjdk-7-jre-headless && curl -L
http://jruby.org.s3.amazonaws.com/downloads/$JRUBY_VERSION/jruby-
bin-$JRUBY_VERSION.tar.gz | tar zxf - && gem install norikra --no-ri --no-rdoc
&& apt-get -y remove build-essential && apt-get -y autoremove && apt-get -y
clean  
  
ENTRYPOINT [ "/jruby-$JRUBY_VERSION/bin/norikra", "start", "--
stats=/var/norikra/stats.json", "--dump-stat-interval=60" ]  
CMD ["--small"]  
  
EXPOSE 26571 26578  
VOLUME ["/var/norikra"]  
  

