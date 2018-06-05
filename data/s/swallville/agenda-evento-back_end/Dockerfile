FROM alpine:3.5  
ENV BUILD_PACKAGES postgresql-dev build-base pkgconfig postgresql-client vim  
  
RUN apk update && \  
apk add --no-cache python python-dev nginx apache2-utils tzdata build-base
ncurses-dev bash --update libmagic && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools && \  
pip install readline && \  
rm -r /root/.cache && \  
rm -f /etc/nginx/conf.d/*  
  
COPY ./inputrc /etc/inputrc  
  
RUN mkdir -p /var/interlegis/agenda && \  
apk add --update --no-cache $BUILD_PACKAGES && \  
mkdir -p /var/interlegis/agenda/static && \  
mkdir -p /var/interlegis/agenda/media/pdf  
  
WORKDIR /var/interlegis/agenda  
  
ADD . /var/interlegis/agenda  
  
COPY start.sh /var/interlegis/agenda/  
COPY config/nginx/agenda.conf /etc/nginx/conf.d  
COPY config/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY env_docker /var/interlegis/agenda/agenda/.env  
  
RUN pip install -r /var/interlegis/agenda/requirements/dev-requirements.txt
--upgrade setuptools && \  
rm -r /root/.cache  
  
# Configura timezone para BRT  
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \  
echo "America/Sao_Paulo" > /etc/timezone  
  
RUN python manage.py collectstatic --noinput && \  
python manage.py crontab add  
  
RUN chmod +x /var/interlegis/agenda/start.sh && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/interlegis/agenda/data", "/var/interlegis/agenda/media/pdf"]  
  
CMD ["/var/interlegis/agenda/start.sh"]  

