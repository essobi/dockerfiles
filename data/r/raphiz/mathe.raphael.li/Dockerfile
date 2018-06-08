FROM ruby:2.3  
RUN apt-get update  
RUN apt-get install -y node python3-pygments  
RUN gem install jekyll rdiscount kramdown  
  
# Python for FTP deployment...  
RUN apt-get install --force-yes -y python3  
  
# Install assets plugin  
RUN gem install jekyll-assets  
RUN gem install uglifier  
RUN gem install redcarpet  
RUN gem install jekyll-sitemap  
RUN gem install jekyll-lunr-js-search  
  
# Working directory  
RUN mkdir /src  
WORKDIR /src  
  
# Create new user jekyll - to prevent user id issues  
RUN groupadd -g 1000 jekyll  
RUN useradd --home /src -u 1000 -g 1000 -M jekyll  
  
# Install lftp for deployment  
RUN apt-get install lftp  

