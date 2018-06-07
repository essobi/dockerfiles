FROM continuumio/miniconda3  
RUN conda install dask distributed boto3 -y  
RUN conda install -c conda-forge iris -y  
RUN conda install -c conda-forge pika -y  
RUN mkdir /app  
COPY src /app  
WORKDIR /app  
CMD python3 -u process.py  

