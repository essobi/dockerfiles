FROM nginx:1.9.5  
EXPOSE 80  
ENV HHVM_VERSION 3.10.1~jessie  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
RUN echo deb http://dl.hhvm.com/debian jessie main | tee
/etc/apt/sources.list.d/hhvm.list  
RUN apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q supervisor less
hhvm=$HHVM_VERSION \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
ADD default.conf /etc/nginx/conf.d/default.conf  
CMD supervisord -e debug  

