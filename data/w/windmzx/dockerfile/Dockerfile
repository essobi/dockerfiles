FROM ubuntu:16.04  
MAINTAINER mzx 2281927774@qq.com  
RUN apt-get update --fix-missing && apt-get install -y git && apt-get clean  
RUN git clone https://github.com/ssrbackup/shadowsocksr /usr/ssr  
  
CMD ["python","/usr/ssr/shadowsocks/local.py","-c","/etc/shadowsocks.json"]

