FROM docker:stable  
  
ENV CLI_VERSION=1.15.10  
  
RUN apk -v --update add \  
python \  
py-pip \  
groff \  
less \  
mailcap \  
&& \  
pip install --upgrade awscli==$CLI_VERSION && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  
  

