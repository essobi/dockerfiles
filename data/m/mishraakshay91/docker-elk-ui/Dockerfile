FROM debian:wheezy  
MAINTAINER mishra.akshay91@gmail.com  
  
######## ADD REQUIRED NGINX PACKAGES AND FETCH KEYS #########  
RUN echo "deb http://nginx.org/packages/debian/ wheezy nginx" >>
/etc/apt/sources.list.d/nginx.list  
RUN apt-key adv --fetch-keys "http://nginx.org/keys/nginx_signing.key"  
  
####### UPDATE APT REPOSITORIES ########  
RUN apt-get update && apt-get -y dist-upgrade  
  
####### INSTALL NGINX OPENSSL AND CERTFICATES SUPPORT #######  
RUN apt-get -y install nginx openssl ca-certificates  
  
####### REMOVE DEFAULT CONFIG FILES FOR NGINX #########  
RUN rm -rf /etc/nginx/conf.d/*  
  
####### REMOVE DEFAULT SOURCE PAGES FOR NGINX ########  
RUN rm -rf /srv/www/*  
  
####### ADD CUSTOM NGINX CONF #########  
ADD config/nginx.conf /etc/nginx/nginx.conf  
  
####### SPECIFY DEFAULT NGINX CONFIG SETTINGS IN THIS FILE AND ADD TO
CONTAINER #####  
ADD config/default.conf /etc/nginx/conf.d/default.conf  
  
###### ADD CUSTOM PAGE THAT YOU WANT TO RENDER ON PORT 80  
ADD custompages/responseplot.html /srv/www/responseplot.html  
ADD custompages/urlplot.html /srv/www/urlplot.html  
  
###### MOUNTING VOLUMES TO SPIN UP THE CONTAINER USING CUSTOM SOURCE CODE AND
CONFIG  
###### NOT OF MUCH USE IN OUR CASE THOUGH  
#VOLUME ["/etc/nginx"]  
#VOLUME ["/srv/www"]  
  
##### EXPOSE PORTS TO BE PUBLISHED TO THE HOST  
EXPOSE 80  
#EXPOSE 443  
  
###### ENTRYPOINT  
ENTRYPOINT ["nginx"]  
#CMD []  

