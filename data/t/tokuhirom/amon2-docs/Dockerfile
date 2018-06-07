FROM ubuntu:16.04  
  
RUN echo "deb http://jp.archive.ubuntu.com/ubuntu/ xenial main restricted\n\  
deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial main restricted\n\  
deb http://jp.archive.ubuntu.com/ubuntu/ xenial-updates main restricted\n\  
deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial-updates main restricted\n\  
deb http://jp.archive.ubuntu.com/ubuntu/ xenial universe\n\  
deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial universe\n\  
deb http://jp.archive.ubuntu.com/ubuntu/ xenial-updates universe\n\  
deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial-updates universe\n\  
deb http://jp.archive.ubuntu.com/ubuntu/ xenial multiverse\n\  
deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial multiverse\n\  
deb http://jp.archive.ubuntu.com/ubuntu/ xenial-updates multiverse\n\  
deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial-updates multiverse\n\  
deb http://jp.archive.ubuntu.com/ubuntu/ xenial-backports main restricted
universe multiverse\n\  
deb-src http://jp.archive.ubuntu.com/ubuntu/ xenial-backports main restricted
universe multiverse\n\  
deb http://security.ubuntu.com/ubuntu xenial-security main restricted\n\  
deb-src http://security.ubuntu.com/ubuntu xenial-security main restricted\n\  
deb http://security.ubuntu.com/ubuntu xenial-security universe\n\  
deb-src http://security.ubuntu.com/ubuntu xenial-security universe\n\  
deb http://security.ubuntu.com/ubuntu xenial-security multiverse\n\  
deb-src http://security.ubuntu.com/ubuntu xenial-security multiverse\n">
/etc/apt/sources.list  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y ca-certificates git openssl nginx
python-sphinx make \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8443  
  
RUN git clone https://github.com/tokuhirom/Amon2-Docs.git /amon2-docs  
WORKDIR /amon2-docs  
RUN make html  
  
RUN mkdir -p /usr/share/nginx/logs/  
  
COPY /nginx.conf /nginx.conf  
RUN /usr/sbin/nginx -t -c /nginx.conf  
  
CMD /usr/sbin/nginx -c /nginx.conf  

