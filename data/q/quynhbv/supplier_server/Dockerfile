FROM ruby:2.3.1  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && apt-get install
-y nodejs  
  
RUN apt-get update && \  
apt-get install -y openjdk-7-jdk  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
  
RUN export JAVA_HOME  
  
RUN echo $JAVA_HOME  
  
COPY Gemfile /cache/Gemfile  
COPY Gemfile.lock /cache/Gemfile.lock  
  
RUN cd /cache && bundle install  
  
RUN curl -o /usr/bin/framgia-ci https://raw.githubusercontent.com/framgia/ci-
report-tool/master/dist/framgia-ci && chmod +x /usr/bin/framgia-ci  

