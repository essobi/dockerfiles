FROM ruby:2.2.0  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# for postgres  
RUN apt-get install -y libpq-dev  
  
# for mysql  
RUN apt-get install -y libmysqlclient-dev mysql-client  
  
# for nokogiri  
RUN apt-get install -y libxml2-dev libxslt1-dev  
  
# for capybara-webkit  
RUN apt-get install -y libqt4-webkit libqt4-dev xvfb  
  
# for a JS runtime  
RUN apt-get install -y nodejs  
  
# gem requirements  
RUN apt-get install -y freetds-dev  
RUN apt-get install -y imagemagick libmagickwand-dev  
RUN ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/Magick-config
/usr/bin/Magick-config  
  
# set up herokuish  
RUN curl
https://github.com/gliderlabs/herokuish/releases/download/v0.3.2/herokuish_0.3.2_linux_x86_64.tgz
\  
\--silent -L | tar -xzC /bin  
  
RUN /bin/herokuish buildpack install https://github.com/heroku/heroku-
buildpack-ruby \  
&& /bin/herokuish buildpack install https://github.com/heroku/heroku-
buildpack-nodejs \  
&& ln -s /bin/herokuish /build \  
&& ln -s /bin/herokuish /start \  
&& ln -s /bin/herokuish /exec  

