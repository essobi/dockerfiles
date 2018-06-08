FROM 127labs/elixir:latest  
  
MAINTAINER Imran Ismail <imran@127labs.com>  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv D101F7899D41F3C3  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update  
RUN apt-get install -y yarn  
  
COPY ./wait-for-it.sh /tmp  

