FROM codexfons/gunicorn  
  
USER root  
  
RUN apk add --update --virtual=build-dependencies wget ca-certificates
python3-dev postgresql-dev libxml2-dev libxslt-dev build-base  
RUN apk add --update libpq libxml2 libxslt libstdc++  
RUN python3 --version  
  
COPY requirements.txt /requirements.txt  
RUN pip3 install -r /requirements.txt  
  
RUN apk del build-dependencies  
RUN rm -rf /var/cache/apk/*  
  
COPY [a-z_A-Z]* $APP_PATH/  
COPY open_budget_search_api/ $APP_PATH/open_budget_search_api/  
RUN ls -la /opt/app/  
  
USER $GUNICORN_USER  
  
ENV GUNICORN_MODULE=open_budget_search_api.main  
  
EXPOSE 8000  
ENTRYPOINT $APP_PATH/startup.sh  

