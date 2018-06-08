FROM alpine  
RUN apk add --no-cache \  
php7 \  
php7-ctype \  
php7-json \  
php7-mbstring \  
php7-session \  
tar jq curl tini  
# Download and extract source code in one go  
RUN mkdir /app \  
&& curl -L $(curl -s
https://api.github.com/repos/ptrofimov/beanstalk_console/releases/latest
beanstalk_console | jq --raw-output '.tarball_url') | tar xvz -C /app --strip-
components 1 \  
&& chmod o+w /app/storage.json \  
&& echo '$GLOBALS["config"]["servers"] = explode(",", getenv("SERVERS"));' >>
/app/config.php  
  
USER nobody  
EXPOSE 8080  
ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/php7", "-S", "0.0.0.0:8080", "-t",
"/app/public"]  

