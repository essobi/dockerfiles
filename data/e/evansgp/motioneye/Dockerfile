FROM alpine:3.5  
ENV PYCURL_SSL_LIBRARY openssl  
  
RUN apk add --no-cache gcc musl-dev libcurl curl-dev libjpeg jpeg-dev python
python-dev py-pip py-setuptools tzdata && \  
pip install --upgrade pip tornado jinja2 pillow pycurl motioneye && \  
apk --purge -v del python-dev py-pip gcc musl-dev curl-dev jpeg-dev  
  
RUN mkdir /etc/motioneye && \  
cp /usr/share/motioneye/extra/motioneye.conf.sample
/etc/motioneye/motioneye.conf  
  
CMD /usr/bin/meyectl startserver -c /etc/motioneye/motioneye.conf  
  
VOLUME /etc/motioneye  
VOLUME /var/lib/motioneye  
  
EXPOSE 8765  
RUN cp /usr/share/zoneinfo/Australia/Perth /etc/localtime && \  
echo "Australia/Perth" > /etc/timezone  
  

