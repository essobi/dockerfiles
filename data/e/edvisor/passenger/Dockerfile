FROM nodesource/jessie:5.9.0  
  
RUN apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
561F9B9CAC40B2F7 \  
&& sh -c 'echo deb https://oss-binaries.phusionpassenger.com/apt/passenger
jessie main > /etc/apt/sources.list.d/passenger.list' \  
&& apt-get update \  
&& apt-get install -y \--force-yes \--no-install-recommends\  
nginx-extras \  
passenger \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& adduser \--shell /usr/sbin/nologin \--no-create-home \--disabled-login
\--gecos "" \--disabled-password nginx  
  
ADD https://raw.githubusercontent.com/edvisor-io/docker-nginx-
node/master/nginx.conf /etc/nginx/nginx.conf  
  
CMD ["nginx", "-g", "daemon off;"]  

