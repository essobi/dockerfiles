FROM ruby:2.2.0  
RUN apt-get update -qq && \  
apt-get install -y build-essential && \  
rm -rf /var/lib/apt/lists/*  
  
RUN gem install junit_merge -v 0.1.2  
  
RUN mkdir /robot  
  
VOLUME /robot  
WORKDIR /robot  
  
ENTRYPOINT ["junit_merge"]

