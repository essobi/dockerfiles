FROM vicinitycommerce/rails:4.2.1  
MAINTAINER Vicinity Commerce <engineering@vicinitycommerce.com>  
  
# Install Nginx + Passenger  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7
\  
&& apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
&& echo 'deb https://oss-binaries.phusionpassenger.com/apt/passenger trusty
main' > /etc/apt/sources.list.d/passenger.list \  
&& apt-get update && apt-get install -y --no-install-recommends \  
nginx-extras \  
passenger \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Precompile Ruby extensions  
RUN passenger-config build-native-support && rm -rf /tmp/*  
  
# Remove the default site  
RUN rm /etc/nginx/sites-enabled/default  
# Add the nginx configuration  
ADD nginx.conf /etc/nginx/  

