from debian:stretch  
  
RUN apt-get update && apt-get install curl -y  
RUN curl -o /tmp/Diacamma_setup.tar.gz http://www.sd-
libre.fr/download/Diacamma_setup.tar.gz  
RUN cd /tmp && tar zxvf /tmp/Diacamma_setup.tar.gz  
RUN /tmp/Diacamma/install.sh  
RUN cd /var/lucterios2 \  
&& . virtual_for_lucterios/bin/activate \  
&& pip install gunicorn psycopg2-binary  
RUN apt-get install -y locales locales-all  
RUN locale-gen fr_FR.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR:fr  
ENV LC_ALL fr_FR.UTF-8  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

