FROM python:3.5  
ADD requirements.txt /code/requirements.txt  
WORKDIR /code/  
  
RUN pip install -r requirements.txt  
  
ADD . /code  
  
RUN useradd mez  
RUN mkdir /home/mez  
RUN chown -R mez /home/mez  
  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
CMD /usr/local/bin/run  

