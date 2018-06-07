FROM node  
  
ENV PROJECT_DIR=/app  
WORKDIR $PROJECT_DIR  
  
#COPY /html/package.json $PROJECT_DIR  
RUN apt-get update && apt-get install -y \  
&& apt-get install -y vim \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm install  
  
EXPOSE 8888

