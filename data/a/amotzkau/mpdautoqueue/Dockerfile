FROM debian  
  
RUN apt-get update && apt-get install -y --no-install-recommends
python3-musicpd  
  
ADD autoqueue.py /usr/local/sbin/  
  
RUN useradd -m autoqueue  
  
USER autoqueue  
  
ENTRYPOINT ["/usr/local/sbin/autoqueue.py"]  

