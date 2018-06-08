FROM flowmatters/jupyter-spatial  
  
COPY requirements.txt /home/jovyan/requirements_fmpl.txt  
  
USER root  
RUN apt-get update && \  
apt-get install -y cmake openmpi-bin libopenmpi-dev  
  
USER jovyan  
RUN pip install -r /home/jovyan/requirements_fmpl.txt && \  
cd /home/jovyan && \  
wget https://github.com/dtarb/TauDEM/archive/v5.3.8.tar.gz && \  
mkdir .TauDEM && \  
tar xzvf v5.3.8.tar.gz -C .TauDEM --strip-components=1 && \  
cd .TauDEM && \  
mkdir bin && \  
cd bin && \  
cmake ../src && \  
make  
  
ENV PATH="/home/jovyan/.TauDEM/bin:${PATH}"  
CMD start.sh jupyter lab --port=22222  

