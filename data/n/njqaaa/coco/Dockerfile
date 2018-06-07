FROM njqaaa/python3  
  
MAINTAINER hy2900822@126.com  
  
# clone code  
RUN cd /root \  
&& git clone https://github.com/jumpserver/coco.git \  
&& cd /root/coco \  
&& rm -rf .git  
  
ADD requirements.txt /root/coco/requirements/requirements.txt  
RUN pip3 install --upgrade pip \  
&& pip3 install -r /root/coco/requirements/requirements.txt \  
&& pip3 install python-gssapi>=0.6.4  
  
RUN ln -s /usr/local/python-3.5/bin/celery /usr/bin/celery  
RUN sed -i 's/python/python3/g' /root/coco/run_server.py  
ADD config.py /root/coco/config.py  
  
WORKDIR /root/coco  
  
EXPOSE 2222  
ADD supervisord.conf /etc/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

