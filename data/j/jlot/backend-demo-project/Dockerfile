FROM node:latest  
LABEL maintainer="lottier.jm@gmail.com"  
LABEL Description="This image is used to start the back-end demo project"  
  
USER root  
  
WORKDIR demo_project  
COPY . /demo_project  
  
RUN useradd -m back; cd /demo_project  
  
EXPOSE 8081  
CMD ["npm", "run", "start", "--host=0.0.0.0"]

