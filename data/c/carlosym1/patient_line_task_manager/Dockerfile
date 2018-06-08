FROM ubuntu:14.04  
MAINTAINER Carlos Yagüe, carlos.yague@upf.edu  
  
RUN mkdir /home/task  
RUN mkdir /home/input  
RUN mkdir /home/ouput  
  
WORKDIR /home/  
  
ADD . ./task  
  
# Do basic updates  
RUN apt-get update -q && apt-get clean  
  
# Get curl in order to download curl  
RUN apt-get install curl -y  
  
# Install the version of Node.js we need.  
RUN bash -c 'curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -'  
RUN apt-get install -y nodejs  
  
# Add and install Docker  
ENV DOCKER_REFRESHED_AT=2016-05-26T00:44-0500  
RUN apt-get install -qqy curl apt-transport-https  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \  
\--recv-keys 58118E89F3A912897C070ADBF76221572C52609D  
RUN echo deb https://apt.dockerproject.org/repo ubuntu-trusty main \  
> /etc/apt/sources.list.d/docker.list  
RUN apt-get update -qq && apt-get install -qqy docker-engine  
  
#Define additional metadata for our image  
VOLUME /var/run/docker  
  
#install dependencies node.js app  
WORKDIR /home/task  
  
RUN npm install  
RUN npm run build  
  
#WORKDIR /home/task  
#CMD ["sh", "-c","npm run serve ${PATH_FOLDER} redis 6379 ${ENCRYPTION_KEY}
${TIME_INTERVAL} production"]  
CMD ["sh", "-c","npm run serve input_folder=${PATH_INPUT_FOLDER}
output_folder=${PATH_OUPUT_FOLDER} redis_ip=redis redis_port=6379
encryption_key=${ENCRYPTION_KEY} time_interval=${TIME_INTERVAL}
mode=production"]

