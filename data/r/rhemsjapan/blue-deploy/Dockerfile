FROM alpine:3.6  
RUN apk add --no-cache supervisor \  
vim \  
bash \  
curl \  
python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi  
  
RUN pip3 install redis \  
&& pip3 install boto \  
&& pip3 install ConfigParser \  
&& pip3 install requests  
  
RUN rm -r /root/.cache && mkdir -p /root/deploy  
  
COPY hook.py /root/deploy  
COPY receiver.py /root/deploy  
COPY DeploySysFunc.py /root/deploy  
COPY supervisord-rhems-deploy-system.conf /etc/supervisor.d/rhems-deploy-
system.ini  
RUN chmod +x /root/deploy/receiver.py /root/deploy/hook.py  
  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
CMD ["/run.sh"]  

