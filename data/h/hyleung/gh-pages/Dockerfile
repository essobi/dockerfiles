FROM ruby:latest  
MAINTAINER Ho Yan Leung <hy.leung@gmail.com>  
  
RUN apt-get -yqq update && \  
apt-get install -y wget && \  
apt-get install -y nodejs  
  
RUN gem install jekyll && \  
gem install github-pages  
  
RUN mkdir /scripts  
ADD scripts/* /scripts  
RUN chmod a+x /scripts/*.sh  
  
VOLUME /gh-pages  
WORKDIR /gh-pages  
  
EXPOSE 4000  
ENTRYPOINT ["/scripts/jekyll.sh"]  
CMD ["serve"]  

