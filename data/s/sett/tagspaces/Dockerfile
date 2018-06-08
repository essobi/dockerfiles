FROM nginx:1.10  
  
ENV TAGSPACES_VERSION 2.3.0  
  
RUN apt-get update \  
&& apt-get install -y wget unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget
https://github.com/tagspaces/tagspaces/releases/download/v${TAGSPACES_VERSION}/tagspaces-${TAGSPACES_VERSION}-web.zip
\  
&& unzip tagspaces-${TAGSPACES_VERSION}-web.zip \  
&& rm -rf /usr/share/nginx/html \  
&& mv tagspaces /usr/share/nginx/html \  
&& rm -rf tagspaces-${TAGSPACES_VERSION}-web.zip

