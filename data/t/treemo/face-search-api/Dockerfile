FROM bamos/openface  
  
  
RUN pip install flask  
RUN mkdir -p /home/face_search_api  
ADD . /home/face_search_api  
  
ENTRYPOINT ["/home/face_search_api/start.py"]  

