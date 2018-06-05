FROM debian:jessie  
MAINTAINER Steven "hw@zving.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
  
RUN rm -rf /etc/apt/sources.list\  
&& touch /etc/apt/sources.list\  
&& echo 'deb http://mirrors.ustc.edu.cn/debian stable main contrib non-free'
>> /etc/apt/sources.list\  
&& echo 'deb-src http://mirrors.ustc.edu.cn/debian stable main contrib non-
free' >> /etc/apt/sources.list\  
&& echo 'deb http://mirrors.ustc.edu.cn/debian stable-proposed-updates main
contrib non-free' >> /etc/apt/sources.list\  
&& echo 'deb-src http://mirrors.ustc.edu.cn/debian stable-proposed-updates
main contrib non-free' >> /etc/apt/sources.list\  
&& apt-get update \  
&& apt-get install -y wget  
  
RUN wget http://www.cafetime.cc/pgdownload/pagestatic_linux.x86_64.tar.gz \  
&& tar zxvf pagestatic_linux.x86_64.tar.gz\  
&& rm pagestatic_linux.x86_64.tar.gz\  
&& mv pagestatic_linux.x86_64 /usr/local/pagestatic  
  
WORKDIR /usr/local/pagestatic  
  
EXPOSE 3000  
EXPOSE 443  
CMD ["nohup","./page_static_linux_amd64","&"]

