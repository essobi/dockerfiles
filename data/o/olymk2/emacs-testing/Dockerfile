#Base for testing emacs packages in batch mode  
FROM ubuntu:latest  
  
RUN apt update && apt install -y emacs  
  
ENTRYPOINT ["bash", "-c", "sleep infinity;"]  

