FROM jjanzic/docker-python3-opencv  
  
WORKDIR /root  
RUN apt-get install vim -y  
RUN pip install schedule requests numpy pyyaml  
  
ADD . .  
  
ENV CAMERA_NAME default  
  
VOLUME /sentia  
  
CMD ["python3", "-u", "sentia/sentia.py", "configs/config_folder.yml"]  

