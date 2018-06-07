FROM debian:latest  
  
LABEL maintainer="zdm <zdm@softvisio.net>"  
  
USER root  
  
ADD https://www.dropbox.com/download?plat=lnx.x86_64 /root/dropbox.tgz  
  
ADD https://www.dropbox.com/download?dl=packages/dropbox.py
/usr/local/bin/dropbox  
  
WORKDIR /root/  
  
RUN /bin/bash -c ' \  
apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install python ca-certificates wget \  
&& apt-get clean \  
  
&& tar -xzf dropbox.tgz \  
&& rm -f dropbox.tgz \  
&& chmod +x /usr/local/bin/dropbox \  
'  
  
ENTRYPOINT ["/usr/local/bin/dropbox"]  
  
CMD ["status"]  

