FROM ubuntu:latest  
MAINTAINER George Lewis <schvin@schvin.net>  
  
ENV REFRESHED_AT 2015-04-10  
RUN apt-get update --fix-missing -y && apt-get upgrade -y  
RUN apt-get install -y newsbeuter  
  
RUN groupadd rss  
RUN useradd rss -g rss -d /home/rss  
RUN mkdir -p /home/rss/.newsbeuter  
RUN chown -R rss:rss /home/rss  
  
ENV HOME /home/rss  
USER rss  
WORKDIR /home/rss  
  
ENTRYPOINT ["/usr/bin/newsbeuter"]  

