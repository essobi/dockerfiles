FROM rails:4.2.6  
RUN apt-get update; \  
apt-get install vim -y;  
  
WORKDIR /var/www/api  
  
COPY $PWD/ /var/www/api  
  
RUN echo "export TERM=xterm" >> ~/.bashrc  
  
RUN bundle install  
  
RUN apt-get install -y mysql-client;  
  
EXPOSE 80  
CMD rails s -b 0.0.0.0 -p 80  

