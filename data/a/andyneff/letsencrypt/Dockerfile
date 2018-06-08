FROM alpine:3.5 AS stage1  
  
RUN apk --no-cache add python openssl  
  
RUN apk --no-cache add py-virtualenv gcc python-dev openssl-dev libffi-dev
musl-dev  
  
RUN virtualenv /opt/certbot && \  
. /opt/certbot/bin/activate && \  
pip install certbot  
  
# apk del py-virtualenv gcc python-dev openssl-dev libffi-dev musl-dev  
FROM alpine:3.5  
RUN apk --no-cache add python openssl  
  
COPY \--from=stage1 /opt/certbot /opt/certbot  
  
RUN apk --no-cache add python openssl dcron  
  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 443  
CMD ["crond"]

