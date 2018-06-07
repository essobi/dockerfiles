FROM hackmdio/hackmd  
  
# add config  
ADD config.json /hackmd/config.json  
RUN rm -Rf /hackmd/.sequelizerc  
RUN mkdir /hackmd/db  
  
EXPOSE 3000  
CMD ["/bin/bash", "-c", "/hackmd/docker-entrypoint.sh"]  

