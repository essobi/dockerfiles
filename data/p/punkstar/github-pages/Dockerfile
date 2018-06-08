FROM ubuntu:15.04  
MAINTAINER Nick Jones <nick@nicksays.co.uk>  
  
RUN apt-get update \  
&& apt-get -y install build-essential zlib1g-dev ruby-dev ruby nodejs \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
RUN gem update --system  
RUN gem install github-pages -v 134  
  
VOLUME /site  
  
EXPOSE 4000  
WORKDIR /site  
  
ENTRYPOINT ["jekyll"]  

