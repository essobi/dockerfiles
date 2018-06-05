FROM sorgerlab/ashlar:v1.3.0  
RUN pip install awscli ruamel.yaml  
ADD sync_and_run.py /usr/local/bin/sync_and_run.py  
  
RUN mkdir /mnt/input && mkdir /mnt/output  
  
WORKDIR /mnt/output  
  
ENTRYPOINT ["/usr/local/bin/sync_and_run.py"]  

