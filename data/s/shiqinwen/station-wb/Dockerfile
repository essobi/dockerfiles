FROM ubuntu:16.04  
EXPOSE 3000  
RUN bundle config --global frozen 1  
  
COPY ./ ./  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
  
RUN apt-get update \  
&& apt-get install -y libqt4-dev libqtwebkit-dev nodejs imagemagick
ghostscript mongodb-org \  
&& bundle install \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  

