  
FROM dockerfile/ubuntu  
  
RUN apt-get update  
RUN apt-get install -y python-pip  
  
ADD src /tmp/crawler  
  
RUN pip install -r /tmp/crawler/requirements.txt  
  
ENV ROLE rest  
ENV MESSAGING amqp://guest:guest@localhost:5672  
ENV DB mongodb://guest:guest@localhost:24107/tasks  
  
CMD python /tmp/crawler/start.py --role $ROLE \--messaging $MESSAGING \--db
$DB  
  
EXPOSE 5000  

