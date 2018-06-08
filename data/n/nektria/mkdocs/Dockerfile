FROM httpd:2.4  
RUN apt-get update  
RUN apt-get --no-install-recommends install python-pip python-dev build-
essential libyaml-dev git -y  
RUN rm -rf /var/lib/apt/lists/*  
RUN pip install mkdocs  
WORKDIR /app  

