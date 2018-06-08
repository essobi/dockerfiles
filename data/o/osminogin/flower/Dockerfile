FROM python:alpine  
  
ENV PYTHONUNBUFFERED=1  
ENV PYTHONHASHSEED=random  
ENV PYTHONDONTWRITEBYTECODE=1  
RUN pip install flower redis amqp  
  
EXPOSE 5555  
ENTRYPOINT [ "flower" ]  
CMD [ "--port=5555" ]  

