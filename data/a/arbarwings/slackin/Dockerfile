# Pull base image.  
FROM node:9.11  
LABEL maintainer="Melvin Oostendorp <info@arbarwings.nl>"  
LABEL version="1.0"  
  
RUN apt-get update && apt-get install --no-install-recommends --yes wget unzip
\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://github.com/rauchg/slackin/archive/0.14.0.zip  
RUN unzip 0.14.0.zip  
WORKDIR slackin-0.14.0  
RUN npm install --unsafe-perm  
  
EXPOSE 3000  
CMD ./bin/slackin --port $PORT $SLACK_SUBDOMAIN $SLACK_API_TOKEN
$GOOGLE_CAPTCHA_SECRET $GOOGLE_CAPTCHA_SITEKEY  

