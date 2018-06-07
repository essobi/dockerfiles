FROM python:alpine3.6  
RUN pip install requests  
ADD mailgun.py /bin/mailgun  
RUN chmod +x /bin/mailgun  
ENTRYPOINT ["/bin/mailgun"]  

