# Keras v2.1 with MXNet v1.2  
#  
# docker run --rm -it pottava/keras ipython  
# docker run --rm -it -p 80:8888 pottava/keras  
FROM pottava/mxnet:1.2-note  
  
ENV KERAS_VERSION=2.1.6  
RUN pip install wheel \  
&& pip install --ignore-installed --upgrade "keras == ${KERAS_VERSION}" \  
&& find / -depth -type d -name tests -exec rm -rf {} \; \  
&& find / -depth -type d -name test -exec rm -rf {} \; \  
&& find / -depth -type d -name \\__pycache__ -exec rm -rf {} \; \  
&& rm -rf /root/.cache  

