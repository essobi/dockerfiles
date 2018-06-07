FROM judson/php-sink:latest  
RUN apt-get update \  
&& apt-get install mysql-client unixodbc libpq5 -y \  
&& curl -OL
https://github.com/sphinxsearch/sphinx/releases/download/2.2.11-release/sphinxsearch_2.2.11-release-1.jessie_amd64.deb
\  
&& dpkg -i sphinxsearch_2.2.11-release-1.jessie_amd64.deb \  
&& rm -rf sphinxsearch_2.2.11-release-1.jessie_amd64.deb  

