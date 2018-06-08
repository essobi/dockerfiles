# Dockerfile to install qtcreator and x2goxfce  
FROM spielhuus/x2goxfce:1.0.0  
  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get install locales -y  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
RUN apt-get install -y python3-pip python3-dev build-essential  
RUN pip3 install --upgrade pip  
RUN pip3 install tensorflow  
RUN apt-get install -y python3-matplotlib python3-tk  
RUN python3 -m pip install jupyterhub notebook ipykernel  
RUN python3 -m ipykernel install  
RUN pip3 install jupyter  
  
  

