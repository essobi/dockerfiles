FROM python:3.5  
WORKDIR /usr/src/app  
ADD ftapp.py .  
RUN pip install Flask  
RUN pip install boto3==1.4.3  
RUN pip install wheel  
RUN pip install pandas  
RUN chmod 777 /usr/src/app/  
CMD [ "python", "ftapp.py" ]  

