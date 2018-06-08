FROM alpine:3.6  
MAINTAINER Lauser, Nicolai <nicolai@lauser.info>  
  
ENV CWD /ftp  
  
ADD docker-entrypoint.sh /  
  
RUN apk --update add ncftp \  
&& rm -rf /var/cache/apk/* \  
&& chmod 775 /docker-entrypoint.sh \  
&& mkdir -p ${CWD} \  
&& mkdir -p /templates  
  
VOLUME /templates  
WORKDIR ${CWD}  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

