FROM frapontillo/java:7  
MAINTAINER Francesco Pontillo <francescopontillo@gmail.com>  
  
RUN apt-get update -y && apt-get install -y \  
unzip \  
wget  
RUN printf '%s\n%s\n%s\n%s\n' \  
'* - memlock unlimited' \  
'* - nofile 100000' \  
'* - nproc 32768' \  
'* - as unlimited' \  
>> /etc/security/limits.conf  
RUN cd /opt/ \  
&& wget https://download.jetbrains.com/upsource/upsource-2.0.3554.zip \  
&& chmod a+x upsource-2.0.3554.zip \  
&& unzip upsource-2.0.3554.zip \  
&& chmod -R a+rwX /opt/Upsource \  
&& rm upsource-2.0.3554.zip  
  
COPY configure.sh /opt/Upsource/  
RUN chmod +x /opt/Upsource/configure.sh  
  
EXPOSE 8080  
CMD []  
ENTRYPOINT ["/opt/Upsource/bin/upsource.sh", "run"]

