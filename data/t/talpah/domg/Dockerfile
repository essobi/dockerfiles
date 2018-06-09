FROM google/python  
  
EXPOSE 80  
WORKDIR /home/user/application  
  
ADD start.sh /home/user/start.sh  
ADD . /home/user/application  
  
RUN pip install -r requirements.txt  
  
VOLUME ["/home/user/application/services"]  
  
ENV PYTHONUNBUFFERED=0  
CMD ["/home/user/start.sh"]  

