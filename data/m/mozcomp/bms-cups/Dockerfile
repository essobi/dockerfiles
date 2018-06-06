FROM ruby:2.3.4  
MAINTAINER Phil Mulligan 'mozcomp@mozcomp.com.au'  
RUN apt-get update -qq \  
&& apt-get install -y \  
build-essential \  
libsqlite3-dev \  
libcups2 \  
libcups2-dev \  
cups-client \  
nodejs  
  
RUN gem install bundler --version '1.16.0'  
  
# Install Forego  
ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego
/usr/local/bin/forego  
RUN chmod u+x /usr/local/bin/forego  
  
# Configure CUPS client  
COPY cups-client.conf /etc/cups/client.conf  
  
RUN mkdir /app  
WORKDIR /app  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN bundle install  
ADD . /app  
  
COPY start_app.sh /root/start_app.sh  
RUN chmod +x /root/start_app.sh  
  
EXPOSE 3100  
ENTRYPOINT ["/root/start_app.sh"]  
CMD ["forego", "start", "-r"]  
#CMD ["bin/rails", "server", "--binding=0.0.0.0", "--port=3100"]  

