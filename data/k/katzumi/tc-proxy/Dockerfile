FROM centos:7  
  
MAINTAINER katsumi kato "katzumi+github@gmail.com"  
  
  
RUN true && \  
# squid install  
yum install -y squid iproute && \  
# clean  
yum clean all && \  
true  
  
  
RUN true && \  
touch /var/log/squid/access.log && \  
chown -R squid:squid /var/log/squid/ && \  
chown squid:squid /var/run/squid && \  
echo "acl NOCACHE src all" >> /etc/squid/squid.conf && \  
echo "cache deny NOCACHE" >> /etc/squid/squid.conf && \  
# need ./configure --enable-storeio=null,ufs  
#echo "cache_dir null /dev/null" >> /etc/squid/squid.conf && \  
echo "cache_mem 0 MB" >> /etc/squid/squid.conf && \  
echo "maximum_object_size 0 KB" >> /etc/squid/squid.conf && \  
echo "cache_store_log none" >> /etc/squid/squid.conf && \  
echo "visible_hostname localhost" >> /etc/squid/squid.conf && \  
echo "forwarded_for off" >> /etc/squid/squid.conf && \  
echo "request_header_access Referer deny all" >> /etc/squid/squid.conf && \  
echo "request_header_access X-Forwarded-For deny all" >> /etc/squid/squid.conf
&& \  
echo "request_header_access Via deny all" >> /etc/squid/squid.conf && \  
echo "request_header_access Cache-Control deny all" >> /etc/squid/squid.conf
&& \  
echo "access_log stdio:/var/log/squid/access.log common" >>
/etc/squid/squid.conf && \  
echo "strip_query_terms off" >> /etc/squid/squid.conf && \  
squid -k parse && \  
squid -z && \  
true  
  
ARG TC_TYPE=${TC_TYPE:-wifi-b}  
COPY tc/${TC_TYPE}.sh /tc.sh  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
VOLUME ["/var/cache"]  
  
  
EXPOSE 3128/tcp  

