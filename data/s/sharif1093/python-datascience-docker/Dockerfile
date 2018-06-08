FROM kaggle/python:latest  
  
# No further need it, has been added to the base image  
# RUN pip install --upgrade plotly  
RUN apt-get update && \  
apt-get -y install libcanberra-gtk-module && \  
apt-get autoremove -y && apt-get clean  
  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py  
WORKDIR /workspace  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
CMD ["jupyter", "notebook"]  

