from ubuntu  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y python-pip  
RUN pip install flask  
EXPOSE 5000  
CMD ["python", "/root/flasksample.py"]  
ADD flasksample.py /root/

