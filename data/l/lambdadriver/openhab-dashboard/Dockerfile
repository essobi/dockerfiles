FROM ruby  
  
MAINTAINER Dave Snigier <dave@davesnigier.com>  
  
RUN apt update && \  
apt install -y libsqlite3-dev postgresql-server-dev-9.4 nodejs  
  
RUN gem install bundler dashing  
  
RUN git clone 'https://github.com/LambdaDriver/openhab-dashboard.git' /dashing  
  
WORKDIR /dashing  
  
RUN bundle install  
  
COPY run.sh /  
  
VOLUME ["/dashing"]  
  
ENV PORT 3030  
EXPOSE $PORT  
  
CMD ["/run.sh"]

