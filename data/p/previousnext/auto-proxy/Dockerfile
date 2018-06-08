FROM previousnext/base  
MAINTAINER Nick Schuch "nick@previousnext.com.au"  
# Install Nginx.  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
RUN apt-get install -y wget nginx  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
#fix for long server names  
RUN sed -i 's/# server_names_hash_bucket/server_names_hash_bucket/g'
/etc/nginx/nginx.conf  
  
RUN mkdir /app  
WORKDIR /app  
ADD . /app  
  
RUN wget -P /usr/local/bin
https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-
amd64/forego  
RUN chmod u+x /usr/local/bin/forego  
  
RUN wget https://github.com/jwilder/docker-gen/releases/download/0.3.2/docker-
gen-linux-amd64-0.3.2.tar.gz  
RUN tar xvzf docker-gen-linux-amd64-0.3.2.tar.gz  
  
EXPOSE 80  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
CMD ["forego", "start", "-r"]  

