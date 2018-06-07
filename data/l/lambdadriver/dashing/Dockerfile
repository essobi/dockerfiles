FROM ruby  
  
MAINTAINER Dave Snigier <dave@davesnigier.com>  
  
# install packages and dependencies  
RUN apt-get update && apt-get install -y nodejs  
RUN gem install bundler dashing  
  
# This bit is to pre-install the majority of needed gems,  
# yet still allow additional gems to be installed at runtime  
RUN dashing new /root/gems-dashing  
RUN cd /root/gems-dashing && bundle install --system  
  
VOLUME ["/dashing"]  
EXPOSE 3030  
COPY entrypoint.sh /entrypoint.sh  
WORKDIR /dashing  
CMD ["/entrypoint.sh"]

