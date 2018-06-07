FROM ruby:2.2.5  
MAINTAINER Guilherme Heuser Prestes <guilherme.prestes@gmail.com>  
  
RUN git clone https://github.com/tourdedave/the-internet.git app  
WORKDIR /app  
RUN bundle install --quiet  
EXPOSE 5000  
CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "5000"]  

