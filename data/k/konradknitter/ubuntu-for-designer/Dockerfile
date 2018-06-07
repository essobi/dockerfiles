FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y python  
RUN apt-get install -y graphviz  
RUN apt-get install -y default-jre  
RUN apt-get install -y python-pip  
RUN apt-get install -y git  
RUN apt-get install -y subversion  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
RUN pip install sphinxcontrib_plantuml  
RUN pip install sphinx_bootstrap_theme  
  
RUN apt-get install -y sshpass  
RUN apt-get install -y lftp  

