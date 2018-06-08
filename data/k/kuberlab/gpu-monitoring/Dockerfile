FROM tensorflow/tensorflow:latest-gpu  
  
RUN apt-get update  
RUN apt-get install -y curl sudo vim  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
RUN pip install prometheus_client flask docker  
  
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH  
  
ADD ./export_gpu_stats.py /scripts/export_gpu_stats.py  
ADD ./metrics_server.py /scripts/metrics_server.py  
ADD ./export_tensorflow_stats.py /scripts/export_tensorflow_stats.py  
ADD ./logging.conf /scripts/logging.conf  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 8082  
ENTRYPOINT ["/docker-entrypoint.sh"]  

