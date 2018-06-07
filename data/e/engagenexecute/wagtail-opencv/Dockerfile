FROM engagenexecute/opencv-python2  
ENV PYTHONUNBUFFERED 1  
# Requirements have to be pulled and installed here, otherwise caching won't
work  
COPY requirements.txt requirements.txt  
  
RUN pip install -U pip && pip install -r requirements.txt  
CMD ["bash"]  

