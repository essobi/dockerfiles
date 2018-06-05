FROM rlister/ruby:2.1.6  
MAINTAINER Ric Lister, rlister@gmail.com  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y \  
git  
  
WORKDIR /app  
  
## help docker cache bundle  
ADD ./Gemfile /app/  
ADD ./Gemfile.lock /app/  
  
RUN bundle install --without development test  
  
WORKDIR /app  
ADD ./ /app  
  
EXPOSE 9292 5678  
ENTRYPOINT [ "bundle", "exec" ]  
CMD [ "foreman", "start" ]  

