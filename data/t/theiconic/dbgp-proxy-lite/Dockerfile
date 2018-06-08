FROM alpine:3.5  
LABEL "Maintainer"="THE ICONIC ENGINEERING TEAM
<engineering@theiconic.com.au>"  
  
RUN apk --update --no-cache add \  
python \  
py2-pip  
  
RUN pip2 install --upgrade pip && \  
pip2 install --upgrade komodo-python-dbgp  
  
ADD docker-dbgp-entrypoint.sh /usr/local/bin/docker-dbgp-entrypoint  
  
RUN chmod +x /usr/local/bin/docker-dbgp-entrypoint  
  
ENTRYPOINT ["docker-dbgp-entrypoint"]  
  
ENV IDE_PORT=0.0.0.0:9001  
ENV DEBUG_PORT=0.0.0.0:9000  
CMD pydbgpproxy -i ${IDE_PORT} -d ${DEBUG_PORT}  
  
EXPOSE 9000 9001  

