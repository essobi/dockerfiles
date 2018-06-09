FROM continuumio/miniconda3  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get clean -y  
  
COPY environment.yml /tmp/  
RUN conda env create -f /tmp/environment.yml  
  
ENTRYPOINT ["/bin/bash"]  

