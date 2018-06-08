from tensorflow/tensorflow:1.5.0-py3  
  
EXPOSE 5000  
RUN apt-get update  
RUN apt-get install -y git  
  
RUN pip3 install opencv-python  
RUN pip3 install simplejson  
RUN pip3 install Flask  
RUN pip3 install flask-cors  
RUN apt-get install -y libsm6 libxext6 libfontconfig1 libxrender1 python3-tk  
  
ADD tf-pose-estimation /tf-pose-estimation  
WORKDIR /tf-pose-estimation  
RUN pip3 install -r requirements.txt  
  
ENTRYPOINT ["python", "src/run.py"]

