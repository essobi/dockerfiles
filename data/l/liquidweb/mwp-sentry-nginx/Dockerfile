  
############################################################  
# Dockerfile to set up Sentry and nginx  
############################################################  
  
# Set the base image to nginx  
FROM nginx  
  
# Use our config  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# Lay down the SSL cert and key  
ADD run.sh run.sh  
CMD /run.sh  
  
  

