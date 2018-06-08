# MXNet v1.2 with Jupyter notebook  
#  
# docker run --rm -it pottava/mxnet:1.2-note ipython  
# docker run --rm -it -p 80:8888 pottava/mxnet:1.2-note  
FROM pottava/mxnet:1.2  
ENV JUPYTER_VERSION=1.0.0  
# Install Jupyter  
RUN apt-get update && apt-get autoremove -y \  
&& pip install jupyter==${JUPYTER_VERSION} \  
&& find / -depth -type d -name tests -exec rm -rf {} \; \  
&& find / -depth -type d -name test -exec rm -rf {} \; \  
&& find / -depth -type d -name \\__pycache__ -exec rm -rf {} \; \  
&& rm -rf /root/.cache  
  
# Install tini  
RUN wget -q https://github.com/krallin/tini/releases/download/v0.18.0/tini \  
&& chmod +x /tini  
  
WORKDIR /root/notebook  
ADD jupyter_notebook_config.py /root/.jupyter/  
  
ENTRYPOINT ["/tini", "--"]  
CMD ["jupyter", "notebook"]  

