FROM debian:jessie  
  
MAINTAINER Jan Sorensen <jas@praqma.net>  
  
RUN apt-get update  
RUN apt-get install -y curl gcc  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y ruby ruby-dev make nodejs  
RUN gem install jekyll http json rdiscount --no-ri --no-rdoc  
RUN mkdir /data  
  
WORKDIR /data  
  
EXPOSE 4000  
ENTRYPOINT ["jekyll", "serve", "--watch"]  

