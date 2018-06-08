FROM ubuntu:14.04  
MAINTAINER Srdan Kvrgic <zoomix@kvrgic.se>  
  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8 locale  
RUN echo "LANG=\"en_GB.UTF-8\"" > /etc/default/locale  
RUN locale-gen en_GB.UTF-8  
RUN dpkg-reconfigure locales  
  
RUN apt-get update && \  
apt-get install -y \  
wget \  
imagemagick \  
libmagick++-dev \  
libmagic-dev \  
make \  
ruby1.9.3 \  
nano \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone https://github.com/zoomix/sinatra_galleria.git  
  
RUN cd sinatra_galleria && \  
gem install bundler && \  
gem install rake && \  
bundle install  
  
EXPOSE 9292  
ADD ./runner.sh /runner.sh  
RUN chmod a+x runner.sh  
CMD /runner.sh  

