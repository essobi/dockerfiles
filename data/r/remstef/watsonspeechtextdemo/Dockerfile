###  
#  
# Development guide:  
#  
# - run base container and test commands  
#  
# $ docker run -t -i debian:jessie  
#  
# - build the Dockerfile  
#  
# $ docker build -t watson_speechtext .  
#  
# - run the built container (forward port container port 3000 to host port
8080)  
#  
# $ docker run -d -p 8080:3000 --name wst_instance watson_speechtext  
#  
# - run the built container interactively and overwrite the entrypoint  
#  
# $ docker run -t -i --entrypoint bash watson_speechtext  
#  
# - run a bash command in a running container and connect to it  
#  
# $ docker exec -i -t wst_instance bash  
#  
# - check running containers  
#  
# $ docker ps  
#  
# - check existing containers  
#  
# $ docker ps -a  
#  
# - check output of container  
#  
# $ docker logs wst_instance  
#  
# - stop container  
#  
# $ docker stop wst_instance  
#  
# - start existing container  
#  
# $ docker start wst_instance  
#  
# - delete container (force: -f)  
#  
# $ docker rm wst_instance  
#  
# - delete docker image (force: -f)  
#  
# $ docker rmi wst_instance  
#  
# - see further information:  
#  
# https://docker.github.io/engine/reference/  
# https://docker.github.io/engine/reference/builder/  
# https://docs.docker.com/engine/reference/run  
#  
###  
#  
# Create a debian based docker  
#  
FROM debian:jessie  
  
#  
# specify author  
#  
MAINTAINER Steffen Remus  
  
#  
# specify a description  
#  
LABEL Description="This image is used to start the 'WatsonSpeechText' demo
app."  
LABEL Vendor="Language Technology Group"  
LABEL Version="1.0"  
#  
# set default utf8 locale (C is already installed)  
#  
ENV LANG C.UTF-8  
#  
# set the current working directory to be /code  
# (creates directory if it doesn't exist)  
#  
WORKDIR /code  
  
#  
# install requirements  
#  
RUN apt-get update  
RUN apt-get install -y git nodejs npm  
  
#  
# clone git repository into current directory  
#  
RUN git clone https://github.com/tudarmstadt-lt/WatsonSpeechTextDemo.git .  
#  
# install nodejs requirements (defined in package.json)  
#  
RUN npm install  
  
#  
# specify bluemix text-to-speech and speech-to-text credentials passed to this
Dockerfile via --build-arg key=value  
#  
ARG sttuser  
ARG sttpass  
ARG ttsuser  
ARG ttspass  
  
#  
# replace credentials in app.js file  
#  
RUN cat config/default.json | \  
sed "s/<stt_username>/${sttuser}/g" | \  
sed "s/<stt_password>/${sttpass}/g" | \  
sed "s/<tts_username>/${ttsuser}/g" | \  
sed "s/<tts_password>/${ttspass}/g" > config/default.json_ && \  
mv config/default.json_ config/default.json  
  
#  
# provide access to port 3000 (node default)  
#  
EXPOSE 3000  
#  
# specify docker executable; this prints the lines with the usernames and runs
the app!  
#  
ENTRYPOINT cat config/default.json | grep username & nodejs app.js  
  
  

