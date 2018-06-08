FROM paveu/base-webapp  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash && apt-get install -y
nodejs && apt-get install -y build-essential  
  
ENV APP_NAME apimocker  
ENV CELERY_APP apimocker  
ENV DJANGO_SETTINGS_MODULE apimocker.settings  
ENV ENVIRONMENT production  
  
ADD /requirements/base.txt /app/base.txt  
RUN pip install -r /app/base.txt  
  
WORKDIR /app  
ADD . /app/  
  
RUN cd frontend && npm config set registry http://registry.npmjs.org/ && npm
set strict-ssl falsenpm install && npm install && npm rebuild node-sass && npm
run build  
RUN python manage.py collectstatic --no-input --link -v 0

