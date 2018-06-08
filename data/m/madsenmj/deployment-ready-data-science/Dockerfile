FROM madsenmj/deployment-ready-data-science:utils  
  
# Add app-specific details here  
ADD environment.yml /environment.yml  
RUN conda env create -f /environment.yml  
  
ENV CONDA_ENV tensorflow  

