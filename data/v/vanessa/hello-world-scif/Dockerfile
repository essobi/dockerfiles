###############################################  
# SciF Base  
#  
# docker build -t vanessa/hello-world-scif .  
# docker run vanessa/hello-world-scif  
#  
###############################################  
  
FROM continuumio/miniconda3  
  
#######################################################  
# SciF Install  
  
# Can be replaced with pip install scif  
RUN mkdir /code  
ADD . /code  
RUN /opt/conda/bin/pip install scif  
  
# Install the filesystem from the recipe  
RUN scif install /code/hello-world.scif  
  
# SciF Entrypoint  
  
ENTRYPOINT ["scif"]  

