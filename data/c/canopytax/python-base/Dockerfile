FROM python:3.6-alpine  
  
ENV PYTHONPATH=./.pip:/app/.pip:.: \  
DOCKER=True  
  
RUN apk add --no-cache -u\  
bash \  
postgresql-dev \  
gcc \  
make \  
libffi-dev \  
musl-dev \  
musl-utils \  
jpeg-dev \  
freetype \  
git \  
openssh-client \  
freetype-dev && \  
python3 -m pip install -U \  
dumb-init \  
pip \  
gunicorn \  
"invoke==0.13.0"\  
alembic \  
pytest \  
pytest-cov \  
pylint \  
psycopg2 \  
flake8  
  
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
COPY symlinks.sh /  
ONBUILD RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
ONBUILD COPY requirements.txt /app/  
ONBUILD RUN python3 -m pip install -r /app/requirements.txt -t /app/.pip  
ONBUILD COPY . /app/  
  
WORKDIR /app  
CMD ["dumb-init", "/symlinks.sh"]  

