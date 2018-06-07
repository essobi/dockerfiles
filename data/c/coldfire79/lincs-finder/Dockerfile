FROM coldfire79/bsf-py  
  
RUN pip install pandas numba scipy  
  
WORKDIR /tmp  
RUN wget https://github.com/PNNL-Comp-Mass-Spec/LINCS-
Finder/archive/0.1.0.tar.gz && tar -zxvf 0.1.0.tar.gz  
WORKDIR /tmp/LINCS-Finder-0.1.0  
  
CMD ["python", "bsf_server.py", "8081"]  

