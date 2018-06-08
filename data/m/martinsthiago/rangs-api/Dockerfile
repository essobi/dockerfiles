FROM java:8  
MAINTAINER 'Martins <rogue.thiago@gmail.com>'  
ADD . /src  
WORKDIR /src  
  
RUN bash gradlew installDist &&\  
mkdir /app &&\  
mv build/install/*/* /app &&\  
cd /app &&\  
rm -rf /src &&\  
rm -rf ~/.gradle  
  
WORKDIR /app  
  
# TODO: Implement healthcheck  
# See link https://docs.docker.com/engine/reference/builder/#healthcheck  
# HEALTHCHECK  
# Gradle installDist will make two files (eg: script AND script.bat)  
# the command `ls | head -1` will print only the script not ending in .bat...
then  
# exec will run this script which will start the app  
ENTRYPOINT exec "./bin/`ls ./bin | head -1`"

