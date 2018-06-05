from node  
maintainer Jason Kulatunga <jk17@ualberta.ca>  
  
run npm install -g sails \  
&& npm install -g mocha \  
&& npm cache clear  
  
# copy the application files to the image  
workdir /srv/quietthyme.web  
copy . /srv/quietthyme.web  
  
# create the deploy.json variables  
run echo "{\"DEPLOY_SHA\":\""$(git rev-parse HEAD)"\"}" >
/srv/quietthyme.web/config/nconf/deploy.json  
  
run npm install  
  
#finish up  
expose 1337  
cmd ["sails","lift"]  

