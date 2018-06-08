FROM magazineluiza/ubuntu-ml-mean  
MAINTAINER Matheus Pupo  
  
ENV APP portalmlbi  
ENV PATH /usr/bin:/portalmlbi:$PATH  
ENV LD_LIBRARY_PATH /opt/oracle/instantclient  
RUN git clone git@bitbucket.org:bimagazineluiza/$APP.git  
WORKDIR /$APP  
RUN rm -rf /$aAPP/node_modules && rm -rf /$aAPP/public/vendor  
RUN npm install  
RUN bower install --allow-root  
  
ENTRYPOINT ["npm"]  
CMD ["start"]

