FROM scalyr/scalyr-docker-agent  
  
COPY run.sh /scalyr/run.sh  
RUN chmod u+x /scalyr/run.sh  
  
WORKDIR /scalyr  
CMD [ "/scalyr/run.sh" ]  

