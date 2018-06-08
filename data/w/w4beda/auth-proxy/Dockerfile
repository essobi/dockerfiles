FROM nginx:latest  
  
RUN apt-get update && apt-get install -y ruby-full apache2-utils  
RUN gem install mustache  
ADD nginx.conf.mustache /  
ADD add-user.sh.mustache /  
ADD execute.sh /  
  
ENV CONFIG null  
  
CMD chmod +x execute.sh && sleep 1 && ./execute.sh  

