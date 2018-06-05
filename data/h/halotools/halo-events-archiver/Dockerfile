FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.1.1  
MAINTAINER toolbox@cloudpassage.com  
  
ENV HALO_API_HOSTNAME=api.cloudpassage.com  
ENV HALO_API_PORT=443  
  
ENV DROP_DIRECTORY=/var/events  
  
RUN mkdir /app  
COPY ./ /app/  
  
RUN mkdir -p /src/halo-events  
WORKDIR /src/halo-events  
  
WORKDIR /app/tool/  
  
RUN /usr/bin/python2.7 -m pip install \  
boto3==1.5.6 \  
flake8==3.3.0 \  
pytest==3.2.3 \  
pytest-cov==2.5.1 \  
pytest-flake8==0.8.1  
  
RUN /usr/bin/python2.7 \  
-m py.test \  
\--cov=eventslib \  
\--cov-report=term-missing \  
/app/tool/tests -s  
  
################################################################  
  
FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.1.1  
MAINTAINER toolbox@cloudpassage.com  
  
ENV HALO_API_HOSTNAME=api.cloudpassage.com  
ENV HALO_API_PORT=443  
  
ENV DROP_DIRECTORY=/var/events  
  
RUN mkdir /app  
COPY ./ /app/  
  
RUN mkdir -p /src/halo-events  
WORKDIR /src/halo-events  
  
WORKDIR /app/tool/  
  
RUN pip install \  
boto3==1.5.6  
  
RUN mkdir -p $DROP_DIRECTORY  
  
CMD python /app/tool/runner.py  

