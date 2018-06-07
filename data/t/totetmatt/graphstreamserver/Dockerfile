FROM dockerfile/python  
EXPOSE 5000  
RUN git clone https://github.com/totetmatt/graphStreamServer.git  
RUN pip install -r /data/graphStreamServer/req.txt  
CMD python /data/graphStreamServer/graphStreamServer.py  
  

