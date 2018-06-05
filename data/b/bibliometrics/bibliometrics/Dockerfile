FROM python:3.5-alpine  
  
RUN apk add --update curl gcc g++ libffi-dev busybox-suid  
  
# Fix numpy compilation  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
COPY . /app  
WORKDIR /app  
  
RUN pip --no-cache-dir install -r BibliometricsApp/requirements.txt  
  
RUN chown -R nobody:nogroup /app  
  
USER nobody  
  
EXPOSE 8000  
RUN mv /app/BibliometricsApp/config.py.example /app/BibliometricsApp/config.py  
  
RUN /usr/bin/crontab /app/crontab.txt  
  
CMD gunicorn -k gevent --workers 3 --bind 0.0.0.0:8000 run:app
--chdir=BibliometricsApp --log-level INFO --timeout 0  

