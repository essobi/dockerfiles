FROM php:7.2-alpine  
  
RUN apk add \--no-cache wget \  
&& curl -s https://api.github.com/repos/FriendsOfPHP/PHP-CS-
Fixer/releases/latest \  
| grep browser_download_url \  
| cut -d : -f 2,3 \  
| tr -d \" \  
| wget -qi - \  
&& curl -L https://github.com/FriendsOfPHP/PHP-CS-
Fixer/releases/download/latest/php-cs-fixer.phar -o php-cs-fixer \  
&& chmod +x php-cs-fixer.phar \  
&& mv php-cs-fixer.phar /usr/local/bin/php-cs-fixer  
  
WORKDIR "/srv"  
  
CMD ["/usr/local/bin/php-cs-fixer", "fix"]  

