FROM python:3.5-onbuild  
RUN apt-get clean && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get
install -y openssl build-essential xorg libssl-dev  
COPY wkhtmltox-0.12.3_linux-generic-amd64.tar.xz wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz  
RUN tar -xJf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz && cd wkhtmltox &&
chown root:root bin/wkhtmltopdf && cp -r * /usr/  
VOLUME ["/tmp"]  
ENV PYTHONPATH $PYTHONPATH:/usr/src/app  
WORKDIR /usr/src/app  
CMD alembic upgrade head  
CMD gunicorn -c wsgi_config.py application:app -w 3 --timeout 300  
  

