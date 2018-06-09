FROM debian:jessie  
MAINTAINER Ernesto Baez Fildo <ebaezf@gmail.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ca-certificates openssl socat netcat git curl ssh \  
nginx-extras psmisc jq lua-cjson vim libunwind8 gettext libicu52\  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY etc/register /bin/register  
RUN chmod u+rx /bin/register  
COPY etc/update-site /bin/update-site  
RUN chmod u+rx /bin/update-site  
COPY etc/update-demo /bin/update-demo  
RUN chmod u+rx /bin/update-demo  
  
COPY etc/callback /bin/callback  
COPY etc/update_ssh /bin/update_ssh  
RUN chown .www-data /bin/update_ssh && chmod g+rx /bin/update_ssh  
RUN chown .www-data /bin/callback && chmod g+rx /bin/callback  
  
RUN mkdir -p /docker-conf/www  
COPY www/ /docker-conf/www  
COPY etc/nginx/website.conf /docker-conf/remote.conf  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

