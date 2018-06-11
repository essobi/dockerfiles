FROM wordpress:latest  
  
ENV WOOCOMMERCE_VERSION 2.3.7  
ENV WOOCOMMERCE_UPSTREAM_VERSION 2.3.7  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends unzip wget \  
&& wget https://downloads.wordpress.org/plugin/woocommerce.2.3.7.zip -O
/tmp/temp.zip \  
&& cd /usr/src/wordpress/wp-content/plugins \  
&& unzip /tmp/temp.zip \  
&& rm /tmp/temp.zip \  
&& rm -rf /var/lib/apt/lists/*  

