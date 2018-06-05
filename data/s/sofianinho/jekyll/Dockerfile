FROM ruby:2.3  
MAINTAINER Sofiane Imadali <sofiane.imadali@orange.com>  
  
ENV JEKYLL_PORT 4000  
ADD entrypoint.sh /  
VOLUME /mnt  
  
RUN ruby -S gem install jekyll therubyracer &&\  
useradd -ms /bin/bash jekyll  
  
USER jekyll  
EXPOSE $JEKYLL_PORT  
  
CMD ["/entrypoint.sh"]  

