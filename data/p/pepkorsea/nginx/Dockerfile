FROM nginx:1  
MAINTAINER Max Milton <max.milton@pepkor.com.au>  
  
# Copy over configs  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY h5bp/ /etc/nginx/h5bp/  
COPY conf.d/default.conf /etc/nginx/conf.d/default.conf  
  
# Harden image by unsetting SUID on all executables  
RUN for i in `find / -perm +6000 -type f`; do chmod a-s $i; done  
  
CMD ["nginx", "-g", "daemon off;"]  

