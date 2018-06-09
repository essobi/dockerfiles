FROM ubuntu  
MAINTAINER Utsav Kumar  
  
#Install the required packages in the image  
RUN apt-get update  
RUN apt-get install -y nginx  
  
#Open port  
EXPOSE 80  
#Command to execute while starting the container from the image  
CMD ["nginx", "-g", "daemon off;"]  

