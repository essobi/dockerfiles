FROM kuberlab/dealer-shop:base  
  
ADD . /dealer-shop-base  
  
RUN cd /dealer-shop-base \  
&& ./build.sh \  
&& cp -R nginx-conf/* /etc/nginx/ \  
&& gulp build \  
&& mkdir -p /www \  
&& cp -R /dealer-shop-base/dist/* /www/ \  
&& rm -R /dealer-shop-base  
  
FROM nginx:1.11  
COPY \--from=0 /etc/nginx /etc/nginx  
COPY \--from=0 /www /www  
  
EXPOSE 80

