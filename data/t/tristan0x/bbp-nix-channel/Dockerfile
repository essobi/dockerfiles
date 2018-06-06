FROM nginx:1.13.1  
LABEL maintainer="tristan.carel@gmail.com"  
  
RUN apt-get update \  
&& apt-get install -y python python-pip supervisor git \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install python-swiftclient python-keystoneclient \  
&& sed -i 's/^\\(\\[supervisord\\]\\)$/\1\nnodaemon=true/'
/etc/supervisor/supervisord.conf \  
&& rm /usr/share/nginx/html/index.html  
  
COPY build-nixexprs.py /usr/bin  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY nginx.conf /etc/nginx/conf.d/default.conf  
ADD patches /opt/src/nixexprs/patches  
  
RUN /usr/bin/build-nixexprs.py -vv  
CMD ["/usr/bin/supervisord"]  
EXPOSE 80  

