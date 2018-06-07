FROM eboraas/jupyter  
MAINTAINER Ed Boraas <ed@boraas.ca>  
  
RUN /usr/local/bin/pip --no-cache-dir install --upgrade
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0-cp27-none-
linux_x86_64.whl && \  
rm -r /root/.cache/pip/  
  
ENV
LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/nvidia/lib64:/usr/local/cuda/lib:/usr/local/nvidia/lib:${LD_LIBRARY_PATH}  
  
# Jupyter Notebook  
EXPOSE 8888  
# TensorBoard  
EXPOSE 6006  
WORKDIR /mnt/notebooks  
  
CMD ["/bin/sh", "-c", "/usr/local/bin/jupyter-notebook --no-browser
--ip=0.0.0.0 --notebook-dir=/mnt/notebooks"]  
  

