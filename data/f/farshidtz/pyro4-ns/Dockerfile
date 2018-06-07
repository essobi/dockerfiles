FROM python:2.7-alpine  
  
RUN pip install Pyro4 dill  
  
ENV PYRO_SERIALIZERS_ACCEPTED=serpent,json,marshal,pickle,dill  
ENV PYTHONUNBUFFERED=0  
ENTRYPOINT ["pyro4-ns"]  
  
EXPOSE 9090

