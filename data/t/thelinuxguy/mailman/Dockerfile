FROM alpine:3.4  
RUN apk add --update python3 postfix git&& \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
rm -rf /var/cache/apk/* /root/.cache  
  
RUN cd /tmp && \  
git clone \--depth=1 https://gitlab.com/mailman/mailman.git && \  
cd mailman && python3 setup.py install && cd / && rm -rf /tmp/*  
  
EXPOSE 8001  
RUN adduser -D mailman  
USER mailman  
WORKDIR /home/mailman  
  
VOLUME /home/mailman/var  
  
CMD /usr/bin/mailman start -f && tail -f /home/mailman/var/logs/mailman.log  

