FROM alpine  
  
MAINTAINER Steve Kamerman <https://github.com/kamermans>  
LABEL Description="Portable jq instance"  
  
ADD https://github.com/stedolan/jq/releases/download/jq-1.3/jq-linux-x86_64
/usr/local/bin/jq-1.3  
ADD https://github.com/stedolan/jq/releases/download/jq-1.4/jq-linux-x86_64
/usr/local/bin/jq-1.4  
ADD https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
/usr/local/bin/jq-1.5  
COPY resources/jq.sh /opt/jq.sh  
RUN chmod 0755 /usr/local/bin/jq* \  
&& ln -s /usr/local/bin/jq-1.5 /usr/local/bin/jq \  
&& ln -s /lib /lib64 \  
&& ln -s /lib/ld-musl-x86_64.so.1 /lib/ld-linux-x86-64.so.2  
  
ENTRYPOINT ["/opt/jq.sh"]  
  
CMD ["--help"]  

