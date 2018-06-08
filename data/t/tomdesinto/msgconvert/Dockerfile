FROM perl:5.22.2  
ARG msgconvert_version=0.918  
RUN cpan -i MVZ/Email-Outlook-Message-${msgconvert_version}.tar.gz  
COPY ./docker-entrypoint.sh /  
  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["/bin/bash", "/docker-entrypoint.sh"]  
CMD ["--help"]  

