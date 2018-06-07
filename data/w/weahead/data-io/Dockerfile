FROM docker:17.11.0-ce  
  
LABEL maintainer="We ahead <docker@weahead.se>"  
  
ENV AWS_CLI_VERSION=1.14.3\  
PYTHONIOENCODING=UTF-8\  
PAGER=cat  
  
RUN apk --no-cache add \  
groff \  
python2 \  
py2-pip \  
&& pip --no-cache-dir install awscli==${AWS_CLI_VERSION}  
  
COPY root /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

