# TensorFlow v1.8 with Jupyter notebook  
#  
# docker run --rm -it pottava/tensorflow:1.8-note ipython  
# docker run --rm -it -p 80:8888 pottava/tensorflow:1.8-note  
FROM pottava/tensorflow:1.8  
ENV JUPYTER_VERSION=1.0.0  
RUN apk --no-cache add tini \  
&& pip install "jupyter == ${JUPYTER_VERSION}" \  
&& find / -type d -name tests -depth -exec rm -rf {} \; \  
&& find / -type d -name \\__pycache__ -depth -exec rm -rf {} \; \  
&& rm -rf /root/.cache  
  
WORKDIR /root/notebook  
ADD jupyter_notebook_config.py /root/.jupyter/  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["jupyter", "notebook"]  

