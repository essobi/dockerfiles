FROM python:alpine  
MAINTAINER Isulew <netcookies@gmail.com>  
  
RUN apk add \--update curl wget sed bash openssl \  
&& curl -L $(curl -s
https://api.github.com/repos/lukas2511/dehydrated/releases/latest | grep
'browser_download_url.*gz"' | cut -d\" -f4) | tar xz \  
&& mv dehydrated* app && rm -rf dehydrated* && cd app \  
&& pip install dns-lexicon \  
&& wget
https://github.com/lukas2511/dehydrated/raw/master/docs/examples/config \  
&& wget
https://github.com/AnalogJ/lexicon/raw/master/examples/dehydrated.default.sh
-O hook.sh \  
&& chmod +x hook.sh \  
&& sed -i 's/^#HOOK=.*/HOOK=\/app\/hook.sh/g' config \  
&& sed -i 's/^#KEY_ALGO/KEY_ALGO/g' config \  
&& rm -rf /var/cache/apk/*  
  
ADD run.sh /app/  
RUN chmod +x /app/run.sh  
  
WORKDIR /app  
ENTRYPOINT ["/app/run.sh"]  

