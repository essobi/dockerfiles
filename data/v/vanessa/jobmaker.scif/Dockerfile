#########################################  
# SciF Base  
#  
# docker build -t vanessa/jobmaker.scif .  
# docker run vanessa/jobmaker.scif  
#  
#########################################  
  
FROM continuumio/miniconda3  
  
#########################################  
# SciF Install  
  
ADD . /  
RUN /opt/conda/bin/pip install scif  
  
# Install the filesystem from the recipe  
RUN scif install /jobmaker.scif  
  
# SciF Entrypoint  
  
ENTRYPOINT ["scif"]  

