FROM nlescstoryteller/storyteller  
  
VOLUME /data  
  
WORKDIR /src/query-builder-preprocessing  
COPY . /src/query-builder-preprocessing  
RUN chmod +x run_docker_stack.sh  
RUN sync  
  
EXPOSE 4567  
CMD ["./run_docker_stack.sh", "/data"]  

