FROM dockerfile/python  
MAINTAINER Caner Candan <caner@candan.fr>  
  
RUN mkdir -p /app  
WORKDIR /app  
  
# setup passenger  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7  
RUN apt-get -qq update  
RUN apt-get -qqy install apt-transport-https ca-certificates  
RUN echo "deb https://oss-binaries.phusionpassenger.com/apt/passenger trusty
main" > /etc/apt/sources.list.d/passenger.list  
RUN chown root: /etc/apt/sources.list.d/passenger.list  
RUN chmod 600 /etc/apt/sources.list.d/passenger.list  
RUN apt-get -qq update  
  
# install all dependencies  
RUN apt-get -qqy install memcached postgresql python-psycopg2 python-numpy
python-matplotlib nginx-extras passenger git curl gettext  
  
# setup nginx  
RUN { \  
echo; \  
echo '# stay in the foreground so Docker has a process to track'; \  
echo 'daemon off;'; \  
} >> /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
ADD nginx-app.conf /etc/nginx/sites-enabled/  
RUN mkdir -p public  
  
# run  
EXPOSE 80  
CMD ["nginx"]  

