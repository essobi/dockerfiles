FROM ubuntu:14.04.4  
ENV TARGET_DIR=/data  
ENV GIT_BRANCH=master  
RUN apt-get update \  
&& apt-get install -y python-pip python-dev build-essential git \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install --upgrade gitpython==0.3.2.RC1 \  
&& pip install --upgrade boto==2.8.0 \  
&& pip install --upgrade python-dateutil==1.5 \  
&& pip install --upgrade pytz==2012h \  
&& pip install --upgrade python-cloudfiles \  
&& pip install git-bigstore \  
&& rm -rf /tmp/*  
  
# Configure .ssh directory  
RUN mkdir /root/.ssh \  
&& chmod 0600 /root/.ssh \  
&& echo StrictHostKeyChecking no > /root/.ssh/config  
  
# Configure entrypoint  
COPY /docker-entrypoint.sh /  
COPY /docker-entrypoint.d/* /docker-entrypoint.d/  
RUN chmod 755 /docker-entrypoint.sh && chmod -R 755 /docker-entrypoint.d  
  
CMD ["/docker-entrypoint.sh"]  

