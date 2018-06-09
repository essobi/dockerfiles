FROM jupyter/scipy-notebook  
  
ADD install-pyclustering.sh /home/jovyan/  
RUN bash /home/jovyan/install-pyclustering.sh  
ADD requirements.txt /home/jovyan/  
RUN pip install -r requirements.txt  
ENV PYTHONPATH /home/jovyan/pyclustering:${PYTHONPATH}  

