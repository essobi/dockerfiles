FROM ubuntu:16.04  
ADD setup.sh .  
RUN mkdir -p /data /workspace/pollination  
ADD run-pollination.py /data  
RUN /bin/bash setup.sh  
ENTRYPOINT [ "python", "/data/run-pollination.py" ]  

