FROM python:3.4.2  
WORKDIR /var/app  
  
RUN pip3 install virtualenv  
RUN virtualenv /var/app  
RUN /var/app/bin/pip install uwsgi  
  
RUN useradd uwsgi -s /bin/false  
RUN mkdir /var/log/uwsgi  
RUN chown -R uwsgi:uwsgi /var/log/uwsgi  
  
ONBUILD ADD . /var/app  
ONBUILD RUN if [ -f /var/app/packages.txt ]; then apt-get update && cat
/var/app/packages.txt | xargs apt-get install -y; fi  
ONBUILD RUN if [ -f /var/app/requirements.txt ]; then /var/app/bin/pip install
-r /var/app/requirements.txt; fi  
ONBUILD RUN if cat requirements.txt | grep -q -i Django; then
/var/app/bin/python /var/app/manage.py collectstatic --noinput; fi  
  
ENV UWSGI_NUM_PROCESSES 1  
ENV UWSGI_NUM_THREADS 15  
ENV UWSGI_UID uwsgi  
ENV UWSGI_GID uwsgi  
ENV UWSGI_LOG_FILE /var/log/uwsgi/uwsgi.log  
  
EXPOSE 8080  
ADD uwsgi-start.sh /  
  
CMD []  
ENTRYPOINT ["/uwsgi-start.sh"]  

