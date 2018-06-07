FROM python:3.6  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz
/tmp/  
ADD https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh
/usr/bin/  
ENTRYPOINT ["/init"]  
EXPOSE 80  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \  
rm /tmp/s6-overlay-amd64.tar.gz && chmod +x /usr/bin/wait-for-it.sh  
RUN apt-get update && apt-get install -y pwgen nginx-light libffi-dev && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/www/htdocs/* || true  
RUN pip3 install gunicorn dj_database_url mysqlclient && \  
useradd -d /grader -MN -s /bin/false grader && \  
mkdir -p /data/media && chown -R grader /data  
  
COPY . /grader  
  
RUN cd /grader/docker && tar -c * | tar -C /etc -x && cd /grader && rm -r
/grader/docker/ && \  
pip3 install -r requirements.txt && \  
echo "STATIC_ROOT = '/var/www/htdocs/'" > /grader/grader/local_settings.py &&
\  
python3 manage.py collectstatic -l --no-input  

