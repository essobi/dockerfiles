FROM sbneto/phusion-python  
  
COPY 20_environment.sh /etc/my_init.d/20_environment.sh  
  
RUN chmod 755 /etc/my_init.d/20_environment.sh \  
&& pip3 install --no-cache-dir -U s3conf==0.6.0  

