## This dockerfile is used by automated build on Dockerhub to create a docker
image which has pre-pulled the dependencies  
FROM instapartnersprivate/sbt-precached  
  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
  
RUN sbt update  
  
## To avoid code conflict of removed classes  
RUN rm -rf /usr/src/*  
  
EXPOSE 5005

