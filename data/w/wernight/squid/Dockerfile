FROM alpine:3.5  
  
RUN set -x \  
# Install Squid.  
&& apk add --no-cache squid curl \  
# Install dumb-init (to handle PID 1 correctly).  
# https://github.com/Yelp/dumb-init  
&& curl -Lo /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 \  
&& chmod +x /usr/local/bin/dumb-init \  
# Clean-up.  
&& apk del curl  
  
EXPOSE 3128  
  
ENTRYPOINT ["dumb-init"]  
CMD ["squid", "-N"]  

