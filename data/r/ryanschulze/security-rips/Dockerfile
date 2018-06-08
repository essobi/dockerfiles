FROM ryanschulze/alpine-apache-php5:latest  
LABEL maintainer="Ryan Schulze - https://github.com/ryanschulze"  
LABEL description="RIPS 0.55 - static code analysis for PHP"  
  
RUN apk add --no-cache git && \  
cd /app && \  
git clone -b community --single-branch https://github.com/robocoder/rips-
scanner.git ./ && \  
mkdir /code && \  
sed -i "s/'BASEDIR', ''/'BASEDIR', '\/code\/'/" /app/config/general.php && \  
printf "\n<Directory \"/code\">\n\tAllowOverride All\n</Directory>\n" >
/etc/apache2/conf.d/rips.conf && \  
echo "[i] Success"  
  

