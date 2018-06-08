FROM alpine:latest  
  
RUN apk --no-cache add groff less python py2-pip openssl  
# below should install boto3 and boto 2.x as well  
RUN pip install awscli boto  
  
# installs newest ansible, which requires some dev to be installed in order to
compile  
RUN apk --no-cache add gcc g++ autoconf make libffi-dev openssl-dev python-dev
&& \  
pip install ansible==2.2.1 && \  
apk --no-cache del gcc g++ autoconf make libffi-dev openssl-dev python-dev  

