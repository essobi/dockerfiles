FROM debian:jessie  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y bsdmainutils git dnsutils
&&\  
rm -rf /var/lib/apt/lists/*  
  
ENV TESTSSL_VER 2.9.5  
RUN cd /opt &&\  
git clone \--depth 1 --branch ${TESTSSL_VER}
https://github.com/drwetter/testssl.sh.git  
  
USER nobody  
ENTRYPOINT ["/opt/testssl.sh/testssl.sh"]  
CMD ["-h"]  

