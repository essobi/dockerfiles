FROM nginx:mainline  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends --no-install-suggests \  
gnupg \  
&& apt-get install -y \--no-install-recommends --no-install-suggests \  
apt-transport-https lsb-release ca-certificates curl \  
&& curl -sL https://packages.sury.org/php/apt.gpg | apt-key add \- \  
&& echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
php7.1-fpm php7.1-sqlite3 php7.1-xml php7.1-curl php7.1-gd php7.1-imap \  
php7.1-json php7.1-mbstring php7.1-mcrypt php7.1-pdo php7.1-tidy \  
php7.1-sqlite3 php7.1-simplexml \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/cache/nginx/tmp_proxy  

