FROM alpine:latest  
  
ARG depends="apache2 apache2-mod-wsgi py-pip"  
ARG make_depends="build-base git linux-headers openssl-dev python-dev"  
ARG repository="https://git.openstack.org/openstack/horizon.git"  
ARG tag="10.0.1"  
WORKDIR /opt/horizon  
  
RUN apk add --no-cache $depends\  
&& apk add --no-cache $make_depends\  
&& git clone $repository .\  
&& git checkout -b $tag refs/tags/$tag\  
&& pip install --no-cache-dir --upgrade pip\  
&& pip install --no-cache-dir -r requirements.txt\  
&& pip install --no-cache-dir python-memcached\  
&& mkdir -p /run/apache2\  
&& ./manage.py collectstatic --noinput\  
&& ./manage.py make_web_conf --wsgi\  
&& ./manage.py make_web_conf --apache > /etc/apache2/conf.d/horizon.conf\  
&& sed -i "/openstack_dashboard_website/d" /etc/apache2/conf.d/horizon.conf\  
&& chown -R apache:apache .\  
&& apk del --no-cache $make_depends\  
&& rm -rf .git  
  
ADD docker-entrypoint.sh /usr/local/bin  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD httpd -D FOREGROUND  
  
EXPOSE 80  

