FROM alpine:3.6  
RUN apk add --no-cache \  
git \  
python3 python3-dev \  
libldap py3-pyldap \  
libxml2-dev libxml2-utils py3-lxml \  
yarn  
  
RUN mkdir /app  
  
WORKDIR /app  
  
RUN git clone \--recursive https://github.com/adfinis-sygroup/timed-backend  
RUN git clone \--recursive https://github.com/adfinis-sygroup/timed-frontend  
  
# Install and build frontend  
RUN cd /app/timed-frontend && yarn install  
RUN cd /app/timed-frontend && yarn build -prod  
  
# Install and build backend  
RUN sed -e 's/psycopg2.*//' -i /app/timed-backend/requirements.txt  
RUN sed -e 's/django-auth-ldap.*//' -i /app/timed-backend/requirements.txt  
  
RUN pip3 install django-auth-ldap==1.2.11  
  
RUN pip3 install -r /app/timed-backend/requirements.txt  
  
RUN cp /app/timed-backend/timed/settings.py /app/timed-
backend/timed/settings_base.py  
  
# Set some "required" env vars, so we don't have to mess too much  
# with the settings file  
ENV DJANGO_DATABASE_PASSWORD='' \  
DJANGO_SECRET_KEY='muchsecret' \  
DJANGO_ALLOWED_HOSTS='*' \  
DJANGO_HOST_PROTOCOL=http \  
DJANGO_HOST_DOMAIN='*' \  
DJANGO_DEFAULT_FROM_EMAIL=timed@example.org \  
DJANGO_SERVER_EMAIL=timed@example.org  
  
COPY settings.py /app/timed-backend/timed/settings.py  
  
RUN python3 /app/timed-backend/manage.py migrate  
  
RUN python3 /app/timed-backend/manage.py shell -c 'from
timed.employment.models import User; u = User(); u.username = "admin";
u.set_password("admin"); u.is_superuser=True; u.is_staff = True; u.save()'  
  
# singlepage app support  
RUN pip3 install django-spa  
  
RUN mkdir /app/static  
  
RUN python3 /app/timed-backend/manage.py collectstatic  
  
RUN cp -rv /app/timed-frontend/dist/* /app/static/  
  
# Configure entrypoint etc  
EXPOSE 8000  
ENTRYPOINT python3 /app/timed-backend/manage.py runserver 0.0.0.0:8000  

