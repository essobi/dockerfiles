FROM gallarus/libxgboost:latest as libxgboost  
  
FROM gcr.io/tensorflow/tensorflow:latest-gpu-py3  
  
RUN pip --no-cache-dir install \  
joblib \  
jupyterlab \  
seaborn \  
pandas-profiling \  
catboost \  
requests  
  
COPY \--from=libxgboost /home/xgboost /home/xgboost  
RUN cd /home/xgboost/python-package; python setup.py install  
  
RUN mkdir /work  
  
WORKDIR "/work"  
  
COPY run_jupyter.sh /  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
RUN chmod 777 /run_jupyter.sh && chmod 777
/root/.jupyter/jupyter_notebook_config.py  

