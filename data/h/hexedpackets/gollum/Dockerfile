FROM ruby:2.3  
MAINTAINER William Huba <hexedpackets@gmail.com>  
  
RUN apt-get update && apt-get install -y libicu-dev && rm -rf
/var/lib/apt/lists/*  
RUN gem install -N gollum redcarpet org-ruby  
  
# Create wiki user  
RUN adduser --system --home /wiki --no-create-home --disabled-login wiki  
  
VOLUME /wiki  
WORKDIR /wiki  
USER wiki  
EXPOSE 4567  
CMD ["gollum", "--port", "4567"]  

