FROM cabotapp/cabot:latest  
  
ENV DATABASE_URL ''  
ENV CELERY_BROKER_URL ''  
ENV LOG_FILE '/dev/null'  
RUN python manage.py compress  
RUN echo "from django.contrib.staticfiles.urls import staticfiles_urlpatterns"
> /code/cabot/urls.extended.py  
RUN cat /code/cabot/urls.py >> /code/cabot/urls.extended.py  
RUN echo "\nurlpatterns += staticfiles_urlpatterns()\n" >>
/code/cabot/urls.extended.py  
RUN mv -f /code/cabot/urls.extended.py /code/cabot/urls.py  
  
RUN ./manage.py collectstatic --noinput  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  

