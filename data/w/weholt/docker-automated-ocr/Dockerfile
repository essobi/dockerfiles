FROM petronetto/alpine-opencv-python  
  
RUN mkdir /code/  
  
WORKDIR /code/  
RUN mkdir /data/  
ADD service.py /code/  
  
CMD ["python3.6", "service.py"]  

