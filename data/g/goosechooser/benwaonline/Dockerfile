FROM python:3.6 as packages  
COPY requirements.txt .  
RUN pip wheel --wheel-dir=/tmp/wheelhouse -r requirements.txt  
  
FROM python:3.6-alpine3.7 as testing  
COPY requirements-testing.txt .  
COPY \--from=packages requirements.txt .  
COPY \--from=packages /tmp/wheelhouse /tmp/wheelhouse  
  
RUN echo "manylinux1_compatible = True" >> /usr/local/lib/python3.6/site-
packages/_manylinux.py \  
&& pip install --no-index --find-links=/tmp/wheelhouse -r requirements.txt \  
&& pip install -r requirements-testing.txt \  
&& mkdir -p testing/reports  
  
COPY . /testing/  
WORKDIR /testing  
  
FROM python:3.6-alpine3.7  
COPY \--from=packages requirements.txt .  
COPY \--from=packages /tmp/wheelhouse /tmp/wheelhouse  
  
RUN apk --update add file imagemagick  
RUN echo "manylinux1_compatible = True" >> /usr/local/lib/python3.6/site-
packages/_manylinux.py \  
&& pip install --no-index --find-links=/tmp/wheelhouse -r requirements.txt \  
&& rm -rf /tmp/wheelhouse  
  
WORKDIR /usr/src/app  
COPY . .

