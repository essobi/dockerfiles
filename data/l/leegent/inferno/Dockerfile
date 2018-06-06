FROM python:3.6.0  
ENV PYTHONBUFFERED=1 \  
DATABASE_URL=postgres://postgres:postgres@db:5432/postgres \  
SECRET_KEY='yi7kpcu0f7jh7!664qd=_z_6fz65q1d-lqaduto6rr609fin50' \  
DEBUG=False \  
ALLOWED_HOSTS='*' \  
LOG_LEVEL=INFO  
  
WORKDIR /app  
ADD . .  
RUN pip install -r requirements.txt  
RUN python manage.py collectstatic --noinput  
  
CMD ["gunicorn", "inferno.wsgi", "--log-file", "-", "-b", "0.0.0.0:80", "--
access-logfile", "-"]  
EXPOSE 80  

