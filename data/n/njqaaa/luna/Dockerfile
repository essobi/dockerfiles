FROM njqaaa/python3  
  
MAINTAINER hy2900822@126.com  
  
# clone code  
RUN cd /root \  
&& git clone https://github.com/jumpserver/luna.git \  
&& cd /root/luna \  
&& rm -rf .git  
  
RUN pip3 install --upgrade pip \  
&& pip3 install -r /root/luna/requirements/requirements.txt  
  
RUN sed -i 's/python/python3/g' /root/luna/run_server.py  
ADD config.py /root/luna/config.py  
  
WORKDIR /root/luna  
  
EXPOSE 5000  
ADD supervisord.conf /etc/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

