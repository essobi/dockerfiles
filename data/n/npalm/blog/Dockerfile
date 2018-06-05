FROM jekyll/jekyll:3.4.3 AS build  
MAINTAINER Niek Palm <dev.npalm@gmail.com>  
  
WORKDIR /build  
ADD . /build  
RUN jekyll build  
  
FROM nginx:1.13.3-alpine  
COPY \--from=build /build/_site /usr/share/nginx/html  

