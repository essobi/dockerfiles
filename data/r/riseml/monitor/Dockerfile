FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install python3 curl  
  
RUN curl -sSO https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
  
COPY requirements.txt /app/requirements.txt  
RUN pip install -r /app/requirements.txt  
ENV NVIDIA_VISIBLE_DEVICES all  
ENV NVIDIA_DRIVER_DIR /var/lib/nvidia-docker/volumes/nvidia_driver/latest  
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib64:/usr/local/nvidia/lib  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
  
COPY . /app/  
WORKDIR /app  
ENV PYTHONPATH /app  
CMD python3 start_monitor.py  

