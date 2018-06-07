# Copyright 2017 Valentine C  
FROM alpine:3.6  
MAINTAINER Valentine C  
  
RUN apk add --update \  
python-dev \  
py-pip \  
build-base \  
ca-certificates \  
git \  
zlib-dev \  
jpeg-dev \  
&& git clone https://github.com/valentine/hsg-hackdo.git hackdo \  
&& pip install -r hackdo/requirements.txt \  
&& apk del \  
build-base \  
git \  
&& rm -rf /tmp/* /var/cache/apk/* \  
&& cp hackdo/_local_settings.py hackdo/local_settings.py \  
&& cd hackdo && ./manage.py syncdb --all --noinput \  
&& echo "from django.contrib.auth import get_user_model; \  
User = get_user_model(); \  
User.objects.create_superuser('hackdo', 'hsg@example.com', 'demo')" | \  
python manage.py shell  
  
EXPOSE 80  
WORKDIR /hackdo  
  
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:80" ]  

