FROM ruby  
MAINTAINER Razvan Popa <razvan@qcade.com>  
  
RUN apt-get update && apt-get -qqy install build-essential curl git  
  
RUN git clone https://github.com/errbit/errbit.git /opt/errbit  
WORKDIR /opt/errbit  
  
ENV RAILS_ENV production  
RUN bundle install  
  
ENV MONGO_URL mongodb://mongo/errbit_production  
  
EXPOSE 8080  
ENTRYPOINT ["rails", "server", "-b", "0.0.0.0", "-p", "8080"]  

