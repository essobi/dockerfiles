FROM python:3-alpine  
  
RUN pip install joblib crate  
  
ENV THREADS 32  
ENV RANGE 10000  
ENV URL http://crate:4200  
ENV SHARD 4  
ENV REPLICA 1  
WORKDIR /dist  
  
ADD ./ /dist/  
CMD ["python", "run.py"]  

