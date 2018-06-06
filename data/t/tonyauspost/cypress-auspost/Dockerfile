FROM bahmutov/cypress-image:node-6-cypress-deps  
  
# Need Cypress itself  
ENV CYPRESS_VERSION 0.20.1  
RUN npm set progress=false  
RUN npm i -g --loglevel warn typescript \  
&& npm i -g --loglevel warn @types/cypress \  
&& npm i -g --loglevel warn cypress@$CYPRESS_VERSION \  
&& cypress verify \  
&& cypress --version  
  
RUN groupadd -g 10101 bamboo \  
&& useradd -m -r -s /bin/bash -u 10101 -g 10101 -c "Bamboo Service User"
bamboo  
  

