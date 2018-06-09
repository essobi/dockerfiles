FROM python:2-alpine  
  
RUN pip install virtualenv \  
&& mkdir dns \  
&& cd dns \  
&& virtualenv env \  
&& source env/bin/activate \  
&& mkdir config  
RUN pip install octodns==0.8.8  
RUN apk update \  
&& apk add \--no-cache gcc linux-headers musl-dev libffi-dev openssl-dev
libxslt-dev \  
&& pip install azure-common msrestazure azure-mgmt-dns boto3 lxml dyn  
  
CMD /bin/sh

