FROM ruby:2.3.1  
MAINTAINER John Lin <linton.tw@gmail.com>  
  
ENV HOME /root  
  
# Define working directory for downloading source.  
WORKDIR /root  
  
# Download snort-io  
RUN curl -kL https://github.com/hsnl-dev/snort-io/archive/master.tar.gz | tar
-xvz && \  
cd snort-io-master && \  
bundle install && \  
rake db:migrate  
  
# Define working directory for snort-io.  
WORKDIR /root/snort-io-master  
  
EXPOSE 9292  
CMD ["rackup", "-o", "0.0.0.0"]  

