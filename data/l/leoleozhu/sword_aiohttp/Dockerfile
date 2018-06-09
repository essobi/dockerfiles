FROM python:3  
ENV workdir /workdir-sword  
RUN mkdir -p ${workdir}  
WORKDIR ${workdir}  
  
ADD requirements.txt ${workdir}  
RUN pip install -r requirements.txt  
  
ADD app.py ${workdir}  
ADD manage.py ${workdir}  
ADD sword ${workdir}/sword  
  
ENV SERVER_PORT 8080  
EXPOSE ${SERVER_PORT}  
  
ENTRYPOINT ["python", "app.py"]  

