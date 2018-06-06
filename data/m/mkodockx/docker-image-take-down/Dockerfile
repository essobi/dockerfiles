FROM mkodockx/docker-base:latest  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
# Define duration environment variables  
ENV SUSPEND_DURATION nil  
ENV DELAY_DURATION nil  
  
# Define images list variable  
ENV IMAGES_TO_PRESERVE nil  
  
# Inject the take down task  
ADD take-down.sh /take-down.sh  
RUN chmod +x /take-down.sh  
  
# Initially execution  
CMD ["/take-down.sh"]  

