FROM wordpress:latest  
  
ENV WOOCOMMERCE_VERSION 2.5.2  
ENV WOOCOMMERCE_UPSTREAM_VERSION 2.5.2  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends unzip wget \  
&& wget https://downloads.wordpress.org/plugin/woocommerce.2.5.2.zip -O
/tmp/temp.zip \  
&& cd /usr/src/wordpress/wp-content/plugins \  
&& unzip /tmp/temp.zip \  
&& rm /tmp/temp.zip \  
&& rm -rf /var/lib/apt/lists/*  

