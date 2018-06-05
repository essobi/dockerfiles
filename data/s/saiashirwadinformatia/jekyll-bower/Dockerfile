# Ruby-Node based image with Jekyll-Bower support  
FROM ubuntu:latest  
MAINTAINER Rohan Sakhale <rs@saiashirwad.com>  
  
# Update the repository  
RUN apt-get update -y && apt-get install -y wget  
  
# Install nodejs & npm  
RUN apt-get install -y nodejs \  
&& apt-get install -y npm \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install ruby  
RUN apt-get install -y ruby-full  
  
# Install git  
RUN apt-get install -y git  
  
# Install Jekyll  
RUN npm install -g bower \  
&& gem install jekyll \  
&& gem install bundler \  
&& gem install jekyll-bower  
  
CMD ["jekyll", "bundler", "bower"]

