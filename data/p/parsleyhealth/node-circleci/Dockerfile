FROM parsleyhealth/node:8.11.2  
LABEL maintainer="Michael Shick <m@shick.us>"  
  
# Setup env  
ENV DOCKERIZE_VERSION v0.6.1  
# Update apt  
RUN apt-get update  
  
# Install AWS CLI  
RUN apt-get install -y python-dev python-pip  
RUN pip install awscli  
  
# Install dockerize  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

