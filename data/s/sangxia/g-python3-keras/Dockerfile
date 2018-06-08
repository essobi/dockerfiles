FROM tensorflow/tensorflow:1.3.0-devel-py3  
  
RUN pip3 --no-cache-dir install keras  
  
ADD requirements.txt /tmp/requirements.txt  
RUN pip3 install -r /tmp/requirements.txt  
  
ADD xgboost.sh /tmp/xgboost.sh  
RUN sh /tmp/xgboost.sh  
  
ENV TINI_VERSION v0.15.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Tensorboard  
# EXPOSE 6006  
# EXPOSE 8888  
# CMD ["jupyter", "notebook", "--ip=0.0.0.0"]  
RUN ["/bin/bash"]  

