FROM phusion/baseimage:0.10.0  
LABEL maintainer="kenlea <kenlea@163.com>"  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Zeropro Runtime" \  
org.label-schema.description="Zeropro 运行环境" \  
org.label-schema.url="https://github.com/gorouter/src_dockerfile" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/gorouter/src_dockerfile" \  
org.label-schema.vendor="kenlea" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
COPY baseimage-xenialmu.tar.gz /tmp/zeropro.tar.gz  
COPY Hong_Kong /tmp/Hong_Kong  
  
#ENV SSH_AUTHORIZED_KEYS & SSH_PORT --O  
#ENV FRP_TOKEN_KEYS & FRP_BIND_PORT & FRP_BIND_UDP_PORT & FRP_RPIALLOW_PORTS &
\--O  
# FRP_VHOST_HTTP_PORT & FRP_VHOST_HTTPS_PORT &  
# FRP_DASHBOARD_PORT & FRP_DASHBOARD_USER & FRP_DASHBOARD_PASSWD  
#ENV NQNEW_TOKEN_KEYS --O  
#ENV ???_CFGS && ??_CFGS_ --M  
#NOTE: auto boot web-server --C  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
net-tools wget virt-what kmod iputils-ping iproute2 arp-scan nmap \  
&& tar -C / -xzf /tmp/zeropro.tar.gz \  
&& rm -rf /tmp/zeropro.tar.gz \  
&& rm -f /etc/my_init.d/._01_start_zeropro.sh \  
&& ln -s /usr/bin/python3.5 /usr/bin/python \  
&& mkdir -p /usr/share/zoneinfo/Asia \  
&& mv /tmp/Hong_Kong /usr/share/zoneinfo/Asia/Hong_Kong \  
&& rm -rf /etc/localtime \  
&& ln -s /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime \  
&& /sbin/install_clean  
  
WORKDIR /home  

