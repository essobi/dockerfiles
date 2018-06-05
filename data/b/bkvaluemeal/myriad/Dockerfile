FROM alpine:latest  
MAINTAINER Justin Willis <sirJustin.Willis@gmail.com>  
  
COPY myriad /usr/bin/myriad  
  
RUN apk add --update \  
bash \  
bind-tools \  
curl \  
openssl \  
py-pip \  
&& pip install dns-lexicon \  
&& rm -rf /var/cache/apk/* /tmp/* /var/tmp/* \  
&& curl
https://raw.githubusercontent.com/lukas2511/dehydrated/master/dehydrated \  
-o /usr/bin/dehydrated \  
&& chmod +x /usr/bin/dehydrated \  
&& chmod +x /usr/bin/myriad  
  
ENTRYPOINT ["myriad"]  

