FROM python:3.6-alpine as builder  
LABEL maintainer="Ingo Heimbach <i.heimbach@fz-juelich.de>"  
  
RUN apk --no-cache add build-base libffi-dev openssl-dev  
  
WORKDIR /  
COPY . gitlab-registry-usage-rest  
  
RUN pip install --no-cache-dir "file:///gitlab-registry-usage-rest"  
  
FROM python:3.6-alpine  
  
RUN apk --no-cache add libffi openssl  
  
COPY \--from=builder /usr/local/lib/python3.6/site-packages
/usr/local/lib/python3.6/  
COPY \--from=builder /usr/local/bin/gitlab-registry-usage-rest
/usr/local/bin/gitlab-registry-usage-rest  
  
EXPOSE 80  
ENTRYPOINT ["gitlab-registry-usage-rest"]  

