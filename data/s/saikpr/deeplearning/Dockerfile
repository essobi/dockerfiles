FROM nvidia/cuda:8.0-cudnn6-devel  
# Set the working directory to /app  
WORKDIR /tmp  
ADD . /tmp  
RUN bash ./init_install.sh  
WORKDIR /root  
ENTRYPOINT jupyter notebook --no-browser --ip=0.0.0.0 --allow-root
--NotebookApp.token= --notebook-dir='/root'  
EXPOSE 8888 6006

