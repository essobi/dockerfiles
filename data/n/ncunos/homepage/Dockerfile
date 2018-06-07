FROM nginx:1.9  
MAINTAINER Davy <me@davy.tw>  
  
# Basic Requirements  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install git  
  
# Clone the newest application  
RUN git clone https://github.com/NCUNOS/Homepage.git  
  
# Copy into nginx www directory  
RUN rm -rf /usr/share/nginx/html  
RUN cp -r Homepage /usr/share/nginx/html  
  
# Expose 80 port  
EXPOSE 80  
# Run the server on 80 port  
CMD ["nginx", "-g", "daemon off;"]  

