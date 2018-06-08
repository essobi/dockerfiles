# Version 0.01  
FROM ubuntu:14.04  
MAINTAINER SpanishOrangeTeam  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv C3173AA6 \  
&& echo "deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu trusty main" >>
/etc/apt/sources.list  
  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends  
  
RUN apt-get update  
  
RUN apt-get install -y ruby2.2 ruby2.2-dev gcc nodejs ca-certificates make
build-essential autoconf zlib1g-dev  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN gem update bundler  
RUN gem install jekyll  
RUN gem install github-pages  
RUN gem install compass --pre  
RUN gem install sass-media_query_combiner  
RUN gem install autoprefixer-rails  
  
VOLUME ["/spanish_orange"]  
  
WORKDIR /spanish_orange  
  
EXPOSE 4000  
CMD jekyll serve -w -H ${HOSTNAME}  
  

