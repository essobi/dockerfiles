FROM ruby:2.3.3  
MAINTAINER Doli <doli@doli.us>  
  
  
RUN apt-get clean  
RUN rm -r /var/lib/apt/lists/*  
RUN git clone https://github.com/dolicoli/guess-the-number-sinatra.git var/www
\  
&& cd /var/www  
  
RUN apt-get update  
RUN cd /var/www && bundle install  
  
EXPOSE 3000  
WORKDIR /var/www  
  
CMD bundle exec puma -p 3000

