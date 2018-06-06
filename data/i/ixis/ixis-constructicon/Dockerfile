FROM alpine  
  
RUN apk --update add python py-pip && rm -rf /var/cache/apk/*  
RUN pip install flask  
  
COPY app /app  
WORKDIR /app  
  
EXPOSE 5000  
ENTRYPOINT ["python", "main.py"]  

