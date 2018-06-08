FROM magazineluiza/ubuntu-mktplace  
MAINTAINER Matheus Pupo  
  
ENV APP monitor-integration-marketplace  
ENV PATH /usr/bin:/$APPbit:$PATH  
ENV LD_LIBRARY_PATH /opt/oracle/instantclient  
RUN git clone git@bitbucket.org:magazineluiza-ondemand/$APP.git  
WORKDIR /$APP  
RUN npm install  
  
ENTRYPOINT ["npm"]  
CMD ["start"]

