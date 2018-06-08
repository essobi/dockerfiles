FROM jupyter/datascience-notebook  
LABEL maintainer "boberg37@gmail.com"  
ENV REFRESHED_AT 2018-01-23  
USER root  
  
RUN apt-get update \  
&& apt-get install -y \  
texlive-full \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
USER jovyan  
  
WORKDIR /home/jovyan/work  
ADD requirements.txt .  
RUN pip install -r requirements.txt  

