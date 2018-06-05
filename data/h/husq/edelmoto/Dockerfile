FROM ruby:2.5.0  
RUN apt-get update -qq && apt-get install -y \  
build-essential \  
libpq-dev \  
node.js \  
git-core \  
imagemagick \  
libmagickwand-dev  
  
RUN mkdir /app  
WORKDIR /app  
  
ADD . /app  
  
RUN bundle lock --add-platform x86-mingw32 x64-mingw32 x86-mswin32 \  
&& bundle install  

