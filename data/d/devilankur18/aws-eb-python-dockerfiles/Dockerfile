FROM python:2.7.9  
RUN mkdir -p /var/app  
  
WORKDIR /var/app  
  
RUN virtualenv /var/app  
RUN /var/app/bin/pip install --download-cache /src uwsgi  
  
RUN useradd uwsgi -s /bin/false  
RUN mkdir /var/log/uwsgi  
RUN chown -R uwsgi:uwsgi /var/log/uwsgi  
  
ENV UWSGI_NUM_PROCESSES 1  
ENV UWSGI_NUM_THREADS 15  
ENV UWSGI_UID uwsgi  
ENV UWSGI_GID uwsgi  
ENV UWSGI_LOG_FILE /var/log/uwsgi/uwsgi.log  
  
ADD uwsgi-start.sh /  
  
ONBUILD ADD . /var/app  
ONBUILD RUN if [ -f /var/app/requirements.txt ]; then /var/app/bin/pip install
-r /var/app/requirements.txt; fi  
  
EXPOSE 8080  
CMD []  
ENTRYPOINT ["/uwsgi-start.sh"]

