FROM node:latest  
  
RUN mkdir parse  
  
ADD . /parse  
WORKDIR /parse  
RUN npm install  
  
# These need to be set in AWS elastic beanstalk as ENV variables  
#ENV APP_ID setYourAppId  
#ENV MASTER_KEY setYourMasterKey  
#ENV DATABASE_URI setMongoDBURI  
  
# Optional (default : 'parse/cloud/main.js')  
# ENV CLOUD_CODE_MAIN cloudCodePath  
  
# Optional (default : '/parse')  
# ENV PARSE_MOUNT mountPath  
  
EXPOSE 1337  
  
# Uncomment if you want to access cloud code outside of your container  
# A main.js file must be present, if not Parse will not start  
  
# VOLUME /parse/cloud  
  
CMD [ "npm", "start" ]  
  
  
#NOTES for developers  
# When doing development it might be prudent to build your own Docker image
and push it  
# to a repo where is can be pulled from (Referenced in Dockerrun.aws.json
since it might  
# be to slow to wait for it to update on
https://hub.docker.com/r/silintl/bloom-parse-server/  
#  
# To Build the image do something like this.  
# $ docker build -t yourhubdockeraccount/bloom-parse-server .  
#  
# To be able to push it to hub.docker.com log in  
# $ docker login  
#  
# The credentials file would be needed if the repo were private.  
# cat $HOME/.docker/config.json  
#  
# push the repo to the account you logged into (we want this to be
silintl/bloom-parse-server  
# $ docker push yourhubdockeraccount/bloom-parse-server  
#  

