FROM python  
  
ENV PYTHONUNBUFFERED 1  
  
ENV DB_NAME=postgres \  
DB_USER=postgres \  
DB_PASS=postgres \  
DB_HOST=postgres \  
DB_PORT=5432 \  
SMTP_HOST=smtp \  
SMTP_USER=username \  
SMTP_PASS=password \  
WEB_HOST=localhost \  
GMAPS_API=api  
  
RUN mkdir /mossegada_app && mkdir -p /web_restaurants/media/restaurant_images  
COPY ./mossegada_app /mossegada_app/  
WORKDIR /mossegada_app  
  
RUN pip install -r requirements.txt && python manage.py collectstatic
--noinput  
RUN scripts/download_photos.sh  

