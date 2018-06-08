FROM continuumio/miniconda  
  
COPY environment.yml /  
  
RUN conda update -y conda && \  
conda env create -f environment.yml  
  
ADD ./bin /  
ADD ./data /opt/data  
  
RUN tar -xzvf /opt/data/fdh.sqlite.tar.gz -C /opt/data  
  
ENV PATH /opt/conda/envs/shoreline/bin:$PATH  

