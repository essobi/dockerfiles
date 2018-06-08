FROM frolvlad/alpine-scala:2.11  
ADD . /aplus  
ENV PATH "$PATH:/aplus"  
RUN mkdir -p /feedback  
  
RUN apk update && apk add \  
ca-certificates \  
wget \  
curl \  
perl \  
python3 \  
libxtst \  
&& update-ca-certificates  
  
RUN pip3 install requests  
  
RUN cd /aplus \  
&& wget
https://oss.sonatype.org/content/groups/public/org/scalatest/scalatest_2.11/2.2.6/scalatest_2.11-2.2.6.jar
\  
&& wget
https://oss.sonatype.org/content/repositories/releases/org/scalamock/scalamock-
core_2.11/3.6.0/scalamock-core_2.11-3.6.0.jar \  
&& wget
https://oss.sonatype.org/content/repositories/releases/org/scalamock/scalamock-
scalatest-support_2.11/3.6.0/scalamock-scalatest-support_2.11-3.6.0.jar  
  
WORKDIR /submission  

