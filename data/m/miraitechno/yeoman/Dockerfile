FROM node:0.10.35  
  
MAINTAINER Miraitechno, Inc.  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y ruby ruby-compass ruby-sass  
RUN npm install -g yo@1.3.3 \  
bower@1.3.12 \  
grunt-cli@0.1.13 \  
generator-angular@0.10.0 \  
gulp@3.8.10 \  
generator-gulp-angular@0.8.1  
RUN useradd -m -d /home/developer -s /bin/bash developer && \  
mkdir /opt/app && \  
chown developer /opt/app  
WORKDIR /opt/app  
USER developer  
EXPOSE 3000 9000 35729  
CMD ["/bin/bash"]  
  

