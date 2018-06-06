FROM centurylink/ruby-base:2.1.5  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y libsqlite3-dev ca-
certificates  
  
ADD . /tmp  
WORKDIR /tmp  
RUN bundle install --without development  
  
# These instructions are only executed when this image is used as the base for  
# another image. They will be executed immediately after the FROM instruction  
# in the child Dockerfile.  
ONBUILD ADD . /usr/src/app  
ONBUILD WORKDIR /usr/src/app  
ONBUILD ENV RAILS_ENV production  
ONBUILD RUN bundle install --without development test  
ONBUILD EXPOSE 3000  

