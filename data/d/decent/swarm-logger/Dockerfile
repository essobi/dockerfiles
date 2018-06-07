FROM python:2.7.14-alpine3.7  
RUN apk add --no-cache tzdata && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >
/etc/timezone  
COPY . /opt/swarm-logger/  
WORKDIR /opt/swarm-logger/  
RUN pip install -r requirements.txt  
RUN apk update --no-cache  
RUN apk add logrotate  
COPY ./logrotate.conf /etc/logrotate.d/swarm-logger  
CMD /usr/sbin/crond && python ./swarm_logger.py  
VOLUME ["/var/log/swarm-logger"]  

