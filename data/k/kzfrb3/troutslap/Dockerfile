FROM alpine:3.4  
MAINTAINER kzfrb3  
  
RUN apk update && \  
apk add --update python3 \  
python3-dev  
  
RUN mkdir /troutslap  
WORKDIR /troutslap  
  
COPY troutslap.py /troutslap/troutslap.py  
RUN chmod +x /troutslap/troutslap.py  
COPY requirements.txt /troutslap/  
  
RUN pip3 install --upgrade pip \  
-r requirements.txt  
  
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*  
  
EXPOSE 5000  
CMD ["gunicorn", "-b", "0.0.0.0:5000", "troutslap:app", "--log-file=-"]  
# CMD ["python", "troutslap.py"]  

