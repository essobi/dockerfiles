FROM cypress/browsers:chrome65-ff57  
RUN mkdir /runner  
WORKDIR /runner  
  
RUN npm i cypress  
  
COPY run.sh run.sh  
  
ENTRYPOINT [ "/bin/bash", "./run.sh" ]

