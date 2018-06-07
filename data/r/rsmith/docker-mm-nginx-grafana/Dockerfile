FROM nginx  
  
RUN apt-get update && apt-get install -y curl gnupg2  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update && apt-get install -y nodejs  
  
#enable gzip compression  
RUN sed -i "s/#gzip on/gzip on/" /etc/nginx/nginx.conf  
  
COPY get_certs.js /usr/bin/  
COPY package.json /usr/bin/  
COPY run.sh /usr/bin/  
COPY config/nginx.conf /etc/nginx/conf.d/default.conf  
  
CMD /usr/bin/run.sh  

