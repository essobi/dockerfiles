FROM ruby:2.3  
RUN apt-get update  
RUN apt-get install --force-yes -y node  
  
# Python for FTP deployment...  
RUN apt-get install --force-yes -y python3  
  
# Install addons  
RUN gem install jekyll -v 3.6.2  
RUN gem install jekyll-assets -v 2.4.0  
RUN gem install jekyll-sitemap -v 1.1.1  
RUN gem install redcarpet -v 3.4.0  
RUN gem install rouge -v 3.0.0  
RUN gem install uglifier -v 3.2.0  
RUN gem install therubyracer -v 0.12.3  
  
# Working directory  
RUN mkdir /src  
WORKDIR /src  
  
# Create new user jekyll - to prevent user id issues  
RUN groupadd -g 1000 jekyll  
RUN useradd --home /src -u 1000 -g 1000 -M jekyll  

