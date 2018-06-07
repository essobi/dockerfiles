FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.1.4  
  
MAINTAINER toolbox@cloudpassage.com  
  
ENV HALO_API_HOSTNAME=api.cloudpassage.com  
ENV HALO_API_PORT=443  
  
ENV APP_USER=halocelery  
ENV APP_GROUP=halocelery  
  
  
# Install components from pip  
RUN pip install \  
boto3==1.4.3 \  
celery[redis]==4.2.0rc4 \  
docker==2.6.1 \  
flower==0.9.1  
  
# Install expect, so that we can run 'unbuffer'  
RUN apt-get update && \  
apt-get install -y \  
expect  
  
# Copy over the testing script  
COPY run-tests.sh /app/  
  
# Copy over the app  
RUN mkdir -p /app/halocelery  
  
ADD . /app/halocelery  
  
RUN cd /app/halocelery  
  
WORKDIR /app/  
  
# Set the user and chown the app  
RUN groupadd ${APP_GROUP}  
RUN useradd \  
-g ${APP_GROUP} \  
\--shell /bin/sh \  
\--home-dir /app \  
${APP_USER}  
RUN chown -R ${APP_USER}:${APP_GROUP} /app  
  
USER ${APP_USER}  

