FROM fedoraqa/flask-base:24  
COPY . /usr/src/resultsdb  
WORKDIR /usr/src/resultsdb  
EXPOSE 5001  
ENV DEV true  
RUN pip install -r requirements.txt &&\  
bash init_db.sh  
  
CMD ["python", "runapp.py"]  

