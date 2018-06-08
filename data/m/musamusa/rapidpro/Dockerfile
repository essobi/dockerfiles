FROM ubuntu:14.04  
ENV HOME /root  
  
ENV TERM screen-256color  
  
RUN locale-gen --no-purge en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
  
ADD conf/ppa-remove /tmp/ppa-remove  
RUN chmod +x /tmp/ppa-remove  
RUN /tmp/ppa-remove  
  
RUN apt-get update -qq  
  
ADD conf/apt-packages.txt /tmp/apt-packages.txt  
RUN cat /tmp/apt-packages.txt | xargs apt-get --yes --force-yes install  
  
ADD conf/npm-packages.txt /tmp/npm-packages.txt  
RUN cat /tmp/npm-packages.txt | xargs npm install -g  
  
ADD pip-requires.txt /tmp/requirements_requires.txt  
RUN pip install -r /tmp/requirements_requires.txt  
  
ADD pip-freeze.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
WORKDIR /code  
  
COPY ./ /code/  
RUN cp /code/temba/settings.py.docker /code/temba/settings.py  
  
ADD conf/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
RUN mkdir -p /etc/supervisor/conf.d /var/log/supervisor/  
RUN ln -sf /code/conf/supervisor.rapidpro.conf
/etc/supervisor/conf.d/rapidpro.conf  
RUN ln -sf /code/conf/supervisord.conf /etc/supervisor/supervisord.conf  
RUN ln -sf /usr/bin/nodejs /usr/bin/node  
  
EXPOSE 5000  
EXPOSE 8000  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["start"]  

