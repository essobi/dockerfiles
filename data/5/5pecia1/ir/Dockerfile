FROM httpd:2.4  
MAINTAINER 5pecia1 <pdpxdp@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y curl python  
  
RUN curl
https://gist.githubusercontent.com/5pecia1/92feb8a5eeb2a067b9ad1b9cf550bf30/raw/ac83ac282d770ccdd2e15367fe3a388427f76c3e/httpd.conf
> /usr/local/apache2/conf/httpd.conf  
  
RUN mkdir /Python27 && ln -s /usr/bin/python /Python27/ \  
&& chmod a+w -R /usr/local/apache2/htdocs/  
  
EXPOSE 80  
CMD httpd-foreground  

