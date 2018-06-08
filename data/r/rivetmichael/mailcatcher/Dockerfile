FROM ruby:2.2  
MAINTAINER Michaël Rivet <rivet.michael@gmail.com>  
  
RUN gem install mailcatcher  
  
# Expose on port 25 and 80 for SMTP and web interface  
EXPOSE 25 1080  
CMD ["mailcatcher", "--smtp-ip=0.0.0.0", "--smtp-port=25", "--http-
ip=0.0.0.0", "--http-port=1080", "-f"]  

