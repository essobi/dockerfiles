FROM node:8-slim AS node-build  
ARG COMMIT=dev  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/zestedesavoir/zds-site.git /zds \  
&& cd /zds \  
&& git checkout $COMMIT  
  
WORKDIR /zds  
  
RUN yarn install \  
&& yarn run build \  
&& rm -rf node_modules  
  
FROM python:3-stretch  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git python3 python3-setuptools libxml2-dev \  
libxslt-dev libz-dev libjpeg62-turbo libjpeg62-turbo-dev \  
libfreetype6 libfreetype6-dev libffi-dev sqlite3 \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY \--from=node-build /zds /zds  
  
WORKDIR /zds  
  
RUN pip install -rrequirements-prod.txt \  
&& pip install sqlparse  
  
ENV DJANGO_SETTINGS_MODULE="zds.settings.docker_prod"  
COPY settings/temp_docker_prod.py zds/settings/docker_prod.py  
  
RUN mkdir -p /zds-static \  
&& python manage.py collectstatic --noinput --clear  
  
COPY settings/docker_prod.py zds/settings/docker_prod.py  
  
COPY django_entrypoint.sh django_entrypoint.sh  
RUN chmod +x django_entrypoint.sh  
  
CMD ["bash"]  

