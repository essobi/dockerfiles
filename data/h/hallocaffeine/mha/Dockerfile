FROM python:3.6.4  
LABEL maintainer="bjpaat@dailywarrior.ph"  
COPY . /maria  
COPY ./entrypoint.sh /maria/  
WORKDIR /maria  
# Add Environment Variables here  
ENV DJANGO_SETTINGS_MODULE="config.settings.prod"  
EXPOSE 8000  
RUN pip install --no-cache-dir -U -r requirements.txt  
RUN ["chmod", "+x", "/maria/entrypoint.sh"]  
ENTRYPOINT ["/maria/entrypoint.sh"]  
  

