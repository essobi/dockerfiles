FROM ondrejit/micro-opencv-ffmpeg:latest  
  
RUN PYTHONDONTWRITEBYTECODE=0 pip install imutils --disable-pip-version-check
--no-compile --no-cache-dir  
  
WORKDIR /root  
  
COPY detect.py /usr/local/bin  
  
ENTRYPOINT ["python", "/usr/local/bin/detect.py"]  

