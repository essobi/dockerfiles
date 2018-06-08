FROM anapsix/alpine-java:jre8  
  
# Copyright © 2016 Meteogroup  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is
furnished  
# to do so.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
# SOFTWARE.  
#  
#  
# ElasticMQ (http://elasticmq.org) © 2011-2012 SoftwareMill and Adam Warski,  
# licensed under the Apache License 2.0 (http://www.apache.org/licenses/).  
#  
ENV ELASTICMQ_HOME=/opt/elasticmq  
ENV ELASTICMQ_WORK=/var/lib/elasticmq  
  
RUN apk --no-cache --update upgrade &&\  
apk --no-cache --update add openssl &&\  
mkdir -p "$ELASTICMQ_HOME" &&\  
cd "$ELASTICMQ_HOME" &&\  
wget https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-
server-0.13.5.jar -O elasticmq-server.jar  
  
RUN adduser -h "/var/lib/elasticmq" -k /var/empty/ -s /bin/false -D elasticmq
elasticmq  
  
COPY elasticmq.sh /  
  
EXPOSE 9324  
USER elasticmq  
CMD /elasticmq.sh  

