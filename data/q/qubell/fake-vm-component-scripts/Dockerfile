FROM qubell/python-scripting  
  
RUN mkdir /vms && mkdir /volumes  
RUN pip3 install click  
ENV PYTHONPATH=/common  
  
ADD /common/*.py /common/  
ADD /fake-vm/*.py /fake-vm/  
ADD /fake-volume/*.py /fake-volume/  

