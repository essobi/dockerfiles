FROM michaelsauter/ruby:2.2.4  
MAINTAINER Michael Sauter <mail@michaelsauter.net>  
  
RUN sudo apk-install ruby-nokogiri \  
build-base \  
zlib-dev \  
libxml2-dev \  
libxslt-dev \  
sqlite-dev; \  
sudo rm -fr /usr/share/ri  
  
RUN gem install rails  
RUN bundle config build.nokogiri --use-system-libraries  

