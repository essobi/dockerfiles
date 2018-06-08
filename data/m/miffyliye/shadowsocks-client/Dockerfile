FROM centos:7  
MAINTAINER Wang, Tao <i@miffyliye.org>  
  
RUN yum install -y epel-release \  
&& yum update -y \  
&& yum install -y python-pip \  
&& pip install shadowsocks  
  
ENV SERVER example.com  
ENV SERVER_PORT 2048  
ENV LOCAL_PORT 1080  
ENV LOCAL_ADDR 0.0.0.0  
ENV PASSWORD example  
ENV METHOD aes-256-cfb  
ENV TIMEOUT 300  
ENV VERBOSE 1  
EXPOSE $LOCAL_PORT  
  
CMD VERBOSE_PARAM=""; \  
if [ "$VERBOSE" -ge "2" ]; then VERBOSE_PARAM="-vv"; fi; \  
if [ "$VERBOSE" -eq "1" ]; then VERBOSE_PARAM="-v"; fi; \  
if [ "$VERBOSE" -eq "-1" ]; then VERBOSE_PARAM="-q"; fi; \  
if [ "$VERBOSE" -le "-2" ]; then VERBOSE_PARAM="-qq"; fi; \  
/usr/bin/python /usr/bin/sslocal -s "$SERVER" \  
-p "$SERVER_PORT" \  
-l "$LOCAL_PORT" \  
-b "$LOCAL_ADDR" \  
-k "$PASSWORD" \  
-m "$METHOD" \  
-t "$TIMEOUT" \  
"$VERBOSE_PARAM";  

