FROM ubuntu:trusty  
MAINTAINER Elium Tech <tech@elium.tv>  
  
# Prepare  
RUN apt-get update  
RUN apt-get install -y build-essential nodejs libpq-dev python-dev npm git
curl libldap2-dev libsasl2-dev iputils-ping  
  
RUN curl -OL https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
  
# Deploy cabot  
RUN git clone https://github.com/arachnys/cabot.git /cabot  
  
# Install dependencies  
RUN pip install -e /cabot/  
RUN pip install git+git://github.com/reddit/cabot-alert-slack.git  
RUN npm install --no-color -g coffee-script less@1.3 --registry
http://registry.npmjs.org/  
  
ADD fixture.json /cabot/  
ADD run.sh /cabot/  
ADD gunicorn.conf /cabot/gunicorn.conf  
  
# Add nginx conf  
ADD DATA /DATA  
  
# Set env var  
ENV PATH $PATH:/cabot/  
ENV PYTHONPATH $PYTHONPATH:/cabot/  
  
# Cabot settings  
ENV DJANGO_SETTINGS_MODULE cabot.settings  
ENV LOG_FILE /var/log/cabot  
ENV PORT 5000  
ENV ADMIN_EMAIL admin@elium.io  
ENV CABOT_FROM_EMAIL noreply@elium.io  
ENV DEBUG t  
  
ENV DB_TYPE postgres  
ENV DB_HOST db  
ENV DB_PORT 3306  
ENV DB_USER docker  
ENV DB_PASS docker  
  
ENV CB_HOST celerybroker  
ENV CB_PORT 6379  
ENV DJANGO_SECRET_KEY
2FL6ORhHwr5eX34pP9mMugnIOd3jzVuT45f7w430Mt5PnEwbcJgma0q8zUXNZ68A  
  
# Used for pointing links back in alerts etc.  
ENV WWW_HTTP_HOST cabot.elium.io  
ENV WWW_SCHEME https  
  
RUN ["ln","-s","/usr/bin/nodejs","/usr/bin/node"]  
  
EXPOSE 5000  
WORKDIR /cabot/  
CMD . /cabot/run.sh  

