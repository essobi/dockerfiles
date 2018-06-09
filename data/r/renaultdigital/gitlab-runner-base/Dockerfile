FROM docker:17.09.1-ce  
  
RUN apk -Uuv add apk-tools python git openssh curl jq bash wget ca-
certificates make groff less py-pip tar && \  
pip install -U awscli botocore docutils yamllint && \  
rm /var/cache/apk/*  
  
  

