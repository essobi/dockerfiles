FROM nginx  
RUN apt-get -qqy update \  
&& apt-get -qqy install wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN wget https://github.com/Graylog2/graylog2-stream-
dashboard/releases/download/0.90/graylog2-stream-dashboard-0.90.0.tgz \  
&& tar -xvf graylog2*.tgz \  
&& rm -fr /usr/share/nginx/html/* \  
&& mv graylog2*/app/* /usr/share/nginx/html \  
&& rm -fr graylog*  
  

