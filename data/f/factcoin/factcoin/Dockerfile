FROM python:3  
RUN apt-get update  
RUN apt-get install -y libicu-dev  
  
WORKDIR /app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  
  
ENV POLYGLOT_DATA_PATH "/app/shared/"  
ENV DJANGO_SETTINGS_MODULE "factcoin.settings.dev"  
ENV PORT 8000  
EXPOSE 8000  
ENTRYPOINT [ "./run.sh" ]  

