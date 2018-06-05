FROM nginx:mainline-alpine  
  
## We use a Perl-based entrypoint to tweak the configuration based on ENV vars  
## See README for all ENV vars supported  
RUN apk --no-cache add perl  
COPY env_config.pl /usr/local/bin/  
  
COPY nginx.conf.tmpl /etc/nginx/nginx.conf.tmpl  
  
## Rewrite our template file with our ENV-based parameters  
## See README.md to know which vars are required  
ENTRYPOINT ["/usr/local/bin/env_config.pl", "/etc/nginx/nginx.conf.tmpl",
"/etc/nginx/nginx.conf"]  

