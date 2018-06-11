FROM jwilder/nginx-proxy  
  
RUN { \  
echo 'client_max_body_size 100m;'; \  
} > /etc/nginx/conf.d/max_body_size.conf  
  
RUN mkdir -p /etc/nginx/vhost.d  
  
RUN { \  
echo 'if ($request_method = "OPTIONS") {'; \  
echo ' add_header "Access-Control-Allow-Origin" "*";'; \  
echo ' add_header "Access-Control-Allow-Credentials" "true";'; \  
echo ' add_header "Access-Control-Allow-Methods" "GET, POST, OPTIONS, PUT,
DELETE";'; \  
echo ' add_header "Access-Control-Allow-Headers" "Authorization,Content-
Type,Accept,Origin,User-Agent,DNT,Cache-Control,X-Mx-ReqToken,Keep-
Alive,X-Requested-With,If-Modified-Since";'; \  
echo ' add_header "Access-Control-Max-Age" 1728000;'; \  
echo ' add_header "Content-Type" "text/plain charset=UTF-8";'; \  
echo ' add_header "Content-Length" 0;'; \  
echo ' return 204;'; \  
echo '}'; \  
echo 'if ($request_method = "POST") {'; \  
echo ' add_header "Access-Control-Allow-Origin" "*";'; \  
echo ' add_header "Access-Control-Allow-Credentials" "true";'; \  
echo ' add_header "Access-Control-Allow-Methods" "GET, POST, OPTIONS, PUT,
DELETE";'; \  
echo ' add_header "Access-Control-Allow-Headers" "Authorization,Content-
Type,Accept,Origin,User-Agent,DNT,Cache-Control,X-Mx-ReqToken,Keep-
Alive,X-Requested-With,If-Modified-Since";'; \  
echo ' add_header "Access-Control-Max-Age" 1728000;'; \  
echo '}'; \  
echo 'if ($request_method = "GET") {'; \  
echo ' add_header "Access-Control-Allow-Origin" "*";'; \  
echo ' add_header "Access-Control-Allow-Credentials" "true";'; \  
echo ' add_header "Access-Control-Allow-Methods" "GET, POST, OPTIONS, PUT,
DELETE";'; \  
echo ' add_header "Access-Control-Allow-Headers" "Authorization,Content-
Type,Accept,Origin,User-Agent,DNT,Cache-Control,X-Mx-ReqToken,Keep-
Alive,X-Requested-With,If-Modified-Since";'; \  
echo ' add_header "Access-Control-Max-Age" 1728000;'; \  
echo '}'; \  
echo 'if ($request_method = "PUT") {'; \  
echo ' add_header "Access-Control-Allow-Origin" "*";'; \  
echo ' add_header "Access-Control-Allow-Credentials" "true";'; \  
echo ' add_header "Access-Control-Allow-Methods" "GET, POST, OPTIONS, PUT,
DELETE";'; \  
echo ' add_header "Access-Control-Allow-Headers" "Authorization,Content-
Type,Accept,Origin,User-Agent,DNT,Cache-Control,X-Mx-ReqToken,Keep-
Alive,X-Requested-With,If-Modified-Since";'; \  
echo ' add_header "Access-Control-Max-Age" 1728000;'; \  
echo '}'; \  
echo 'if ($request_method = "DELETE") {'; \  
echo ' add_header "Access-Control-Allow-Origin" "*";'; \  
echo ' add_header "Access-Control-Allow-Credentials" "true";'; \  
echo ' add_header "Access-Control-Allow-Methods" "GET, POST, OPTIONS, PUT,
DELETE";'; \  
echo ' add_header "Access-Control-Allow-Headers" "Authorization,Content-
Type,Accept,Origin,User-Agent,DNT,Cache-Control,X-Mx-ReqToken,Keep-
Alive,X-Requested-With,If-Modified-Since";'; \  
echo ' add_header "Access-Control-Max-Age" 1728000;'; \  
echo '}'; \  
} > /etc/nginx/vhost.d/default_location  

