## https://hub.docker.com/r/jupyter/minimal-notebook/  
FROM jupyter/minimal-notebook  
LABEL version="0.1" description="Installs the application of the VTNA project
at the University Koblenz" maintainer="marvinforster@uni-koblenz.de"  
  
USER root  
  
RUN apt-get update  
RUN apt-get -y install ffmpeg  
  
# Create folder for storing the data of the application  
RUN mkdir -p /usr/src/vtna/  
WORKDIR /usr/src/vtna/  
  
## Copy data for frontend into the container  
COPY frontend ./frontend  
RUN chown -R jovyan:1000 /usr/src/vtna/  
  
## User from the minimal notebook  
USER jovyan  
  
## Change to the users home as workdir  
WORKDIR /usr/src/vtna/  
  
## Install required packages for the frontend  
RUN pip install --no-cache-dir -r frontend/requirements.txt --user  
## Install the vtna package with its dependencies  
RUN pip install --no-cache-dir git+https://github.com/marvinf95/vtna.git
--user  
  
# Delete unnacessary files  
RUN rm frontend/requirements.txt  
  
## Add required jupyter extensions for the notebook  
RUN jupyter nbextension enable \--py widgetsnbextension --user && jupyter
nbextension install --py fileupload --user && jupyter nbextension enable \--py
fileupload --user  
  
## Application is exposed on port 8888  
EXPOSE 8888  
## Start notebook  
CMD jupyter notebook --ip 0.0.0.0 --no-browser frontend/vtna.ipynb  

