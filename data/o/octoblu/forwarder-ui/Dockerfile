FROM nginx  
MAINTAINER Octoblu <docker@octoblu.com>  
  
HEALTHCHECK CMD curl --fail http://localhost:80/healthcheck || exit 1  
  
COPY package.json .  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cat package.json \  
| grep version \  
| head -1 \  
| awk -F: '{ print $2 }' \  
| sed 's/[",]//g' \  
| tr -d '[[:space:]]' > .PKG_VERSION  
  
COPY scripts/ scripts/  
COPY templates/ templates/  
  
RUN sed -e \  
"s/PKG_VERSION/$(cat .PKG_VERSION)/" \  
/templates/default.template > \  
/etc/nginx/conf.d/default.conf  
  
RUN cp /templates/*.conf /etc/nginx/conf.d/  
  
CMD [ "./scripts/run-nginx.sh" ]  

