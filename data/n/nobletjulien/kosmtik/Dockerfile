FROM node:0.12-onbuild  
ENV PROJECT_FILE /project/project.yml  
ENV COMMAND serve  
ENV OPTION $PROJECT_FILE  
  
VOLUME ["/project"]  
EXPOSE 6789  
RUN find / -iname index.js  
CMD node index.js $COMMAND $OPTION  

