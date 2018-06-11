FROM debian:stretch  
MAINTAINER joan@wetopi.com  
  
# Get the last LTS https://nodejs.org/en/download/  
ENV WORDPRESS_VERSION 8.9.4  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get install --no-install-recommends -y -q \  
curl build-essential git ca-certificates \  
\  
\  
&& echo "===> Installing Node..." \  
&& mkdir /nodejs \  
&& curl
https://nodejs.org/dist/v${WORDPRESS_VERSION}/node-v${WORDPRESS_VERSION}-linux-x64.tar.gz
| tar xvzf - -C /nodejs --strip-components=1 \  
\  
\  
&& echo "===> Removing unused APT resources..." \  
&& apt-get purge --auto-remove -y curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
ENV PATH $PATH:/nodejs/bin  
  
CMD ["start"]  
ENTRYPOINT ["/nodejs/bin/npm"]  

