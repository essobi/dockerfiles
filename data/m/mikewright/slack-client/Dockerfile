FROM python:2.7  
RUN pip install slackclient  
  
ADD slack_message.py /slack_message.py  
  
ENTRYPOINT ["/slack_message.py"]  
  

