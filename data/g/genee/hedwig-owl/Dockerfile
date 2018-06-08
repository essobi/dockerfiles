FROM alpine:3.3  
RUN apk add --no-cache python3 \  
&& python3 -m ensurepip \  
&& rm -r /usr/lib/python*/ensurepip \  
&& pip3 install --upgrade pip setuptools \  
&& rm -r /root/.cache  
  
ADD . /app  
RUN cd /app/src && python3 setup.py install && rm -rf /app/src && rm -rf
/root/.cache  
  
VOLUME ["/etc/hedwig"]  
EXPOSE 25  
WORKDIR /app  
ENV PATH=/app/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
\  
NEST_ADDR=http://robot.genee.cn OWL_ID=unknown OWL_SECRET=unknown \  
OWL_ADDR=172.17.0.1:25  
CMD ["/usr/bin/hedwig-owl", "-c", "/etc/hedwig/owl.conf.yml"]

