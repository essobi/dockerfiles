FROM node  
LABEL maintainer="talltechdude"  
  
RUN mkdir /open-stage-control  
RUN git clone https://github.com/talltechdude/open-stage-control /open-stage-
control  
WORKDIR /open-stage-control  
RUN cd /open-stage-control && npm install  
RUN npm run postinstall  
  
ADD run.sh /run.sh  
  
EXPOSE 8080  
VOLUME /data  
  
CMD /run.sh  

