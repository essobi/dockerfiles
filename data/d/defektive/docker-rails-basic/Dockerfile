FROM rails:latest  
  
WORKDIR /usr/src/app  
COPY Gemfile /usr/src/app/  
RUN bundle install  
RUN wget -O /bin/forego
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego  
RUN chmod +x /bin/forego  

