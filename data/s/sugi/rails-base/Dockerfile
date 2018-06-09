FROM ruby:2  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt update  
RUN apt -y full-upgrade  
RUN apt -y install libsqlite3-dev  
RUN apt-get clean  
RUN adduser --system --disabled-password --uid 3000 --group --home /app rails  
RUN gem install bundler --no-rdoc --no-ri  
ADD runapp /  
ENV BUNDLE_APP_CONFIG /app/.bundle  
CMD /runapp  

