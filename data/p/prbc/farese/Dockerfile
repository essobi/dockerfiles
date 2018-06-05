FROM debian:stable  
  
# Update and install prereqs  
RUN apt-get update -y  
RUN apt-get install -y git nginx  
  
# Import the nginx configuration file  
ADD config/nginx.conf /etc/nginx/  
  
# Copy the site from git to the webserver root  
RUN mkdir /root/dev  
RUN git clone https://github.com/prbc/farese.git /root/dev/farese  
RUN cp -r /root/dev/farese/* /usr/share/nginx/html/.  
  
# For the webserver, expose port 80  
EXPOSE 80  
# Run nginx when running the container  
CMD nginx  

