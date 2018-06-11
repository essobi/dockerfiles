FROM newtmitch/sonar-scanner:3.0.3-alpine  
  
RUN apk add \--update nodejs nodejs-npm  
  
RUN npm install -g typescript  
# Use bash if you want to run the environment from inside the shell, otherwise
use the command that actually runs the underlying stuff  
#CMD /bin/bash  
CMD sonar-scanner -Dsonar.projectBaseDir=./src
-Dsonar.typescript.exclusions=node_modules/**

