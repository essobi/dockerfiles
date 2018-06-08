FROM tutum/centos  
  
MAINTAINER Maskeva <zhongguoyinhang_17@qq.com>  
  
RUN yum install git -y  
RUN git clone https://github.com/shadowsocksr/shadowsocksr.git /ssr  
  
ENV SSR_PORT 7766  
ENV SSR_PASSWORD gougou  
ENV SSR_PROTOCOL origin  
ENV SSR_OBFS plain  
  
ADD start.sh /usr/bin/start.sh  
RUN chmod 755 /usr/bin/start.sh  
  
EXPOSE $SSR_PORT  
  
CMD ["start.sh"]  

