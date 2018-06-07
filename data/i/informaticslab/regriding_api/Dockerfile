FROM continuumio/miniconda3  
RUN conda install flask boto3 -y  
RUN conda install -c conda-forge pika -y  
RUN mkdir /app  
COPY src /app  
WORKDIR /app  
CMD python -u api.py  

