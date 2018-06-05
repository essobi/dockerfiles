FROM adsabs/base-microimage:v1.0.1  
ADD ./ /app  
WORKDIR /app  
  
# Provision the project  
RUN pip install -r requirements.txt  
  
EXPOSE 80  
# insert the local config  
ADD local_config.py /local_config.py  
RUN /bin/bash -c "find . -maxdepth 2 -name config.py -exec /bin/bash -c 'echo
{} | sed s/config.py/local_config.py/ | xargs -n1 cp /local_config.py' \;"  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN cp /base/gunicorn.sh /app/gunicorn.sh  
RUN cp /base/gunicorn_entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

