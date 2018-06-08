FROM node:latest  
  
RUN apt-get update && apt-get install -qq -y vim git curl net-tools  
  
ENV PROJECT_PATH /project  
RUN mkdir -p $PROJECT_PATH  
  
WORKDIR $PROJECT_PATH  
  
USER root  
CMD ["bash"]  

