# Dockerfile for light-weight data-filter  
FROM openwhisk/dockerskeleton  
  
ENV FLASK_PROXY_PORT 8080  
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip
build-base wget freetype-dev libpng-dev openblas-dev  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
RUN pip2.7 install numpy  
RUN pip2.7 install sendgrid  
RUN pip2.7 install delorean  
RUN pip2.7 install pymongo  
  
### Add source file(s)  
RUN rm /action/exec  
ADD detectpeaks.py /action/  
ADD mail_settings.py /action/  
ADD exec /action/  
RUN chmod +x /action/exec  
  
CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]  

