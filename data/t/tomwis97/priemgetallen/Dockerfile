FROM alpine  
RUN apk update && \  
apk add python3 py3-flask curl && \  
adduser -S master  
RUN mkdir /data && \  
chown master /data  
USER master  
COPY master.py /master.py  
COPY config.ini /data/config.ini  
RUN python3 /master.py & proc=$! && sleep 3 && curl -i
http://localhost:5000/api/init && kill -s SIGINT $proc  
VOLUME /data  
EXPOSE 5000  
CMD python3 /master.py  

