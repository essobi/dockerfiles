FROM jenkins  
  
USER root  
RUN apt-key update -y  
RUN apt-get update && apt-get install -y python-pip  
RUN pip install mkdocs  
RUN pip install mkdocs-material  
RUN mkdir docs  
  
WORKDIR /docs  
VOLUME /docs  
EXPOSE 8000  
USER jenkins  

