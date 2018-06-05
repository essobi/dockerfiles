FROM masterandrey/docker-matplotlib  
  
COPY pip.requirements.txt /pip.requirements.txt  
  
RUN pip install -r pip.requirements.txt \  
&& rm -rf ~/.pip/cache/ \  
&& rm -rf /var/cache/apk/*  
  
COPY src /iot_calendar/  
  
EXPOSE 4444  
WORKDIR /iot_calendar  
  
CMD ["python3", "iot_calendar.py"]  

