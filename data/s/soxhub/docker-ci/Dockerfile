FROM docker:17-git  
  
RUN apk add --no-cache \  
curl \  
openssl \  
bash  
  
ADD https://codecov.io/bash /bin/codecov  
RUN chmod +x /bin/codecov  

