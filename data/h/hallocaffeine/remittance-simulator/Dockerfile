FROM python:3.6.1  
LABEL maintainer "Bj Paat <bjpaat@dailywarrior.ph>"  
COPY ./mayannah /mayannah  
COPY ./entrypoint.sh /mayannah/  
WORKDIR /mayannah  
RUN pip install --no-cache-dir -r requirements.txt  
EXPOSE 8000  
ENV DJANGO_SETTINGS_MODULE config.settings.prod  
RUN ["chmod", "+x", "/mayannah/entrypoint.sh"]  
ENTRYPOINT ["sh","/mayannah/entrypoint.sh"]  

