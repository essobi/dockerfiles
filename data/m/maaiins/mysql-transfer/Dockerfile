FROM alpine:3.6  
MAINTAINER Lauser, Nicolai <nicolai@lauser.info>  
  
ENV CWD /sql  
  
ADD docker-entrypoint.sh /  
  
RUN apk add --update mysql-client \  
&& rm -rf /var/cache/apk/* \  
&& chmod 775 /docker-entrypoint.sh \  
&& mkdir -p ${CWD}  
  
VOLUME ${CWD}  
WORKDIR ${CWD}  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

