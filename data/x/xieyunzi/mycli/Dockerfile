FROM python:2.7-alpine  
  
RUN apk \--update add \--upgrade \--no-cache \--virtual .build-deps build-base
mysql-dev \  
&& apk \--update add \--upgrade \--no-cache bash mysql-client \  
&& pip install mycli>=1.9 \  
&& apk del .build-deps  
  
CMD ["/bin/bash"]  

