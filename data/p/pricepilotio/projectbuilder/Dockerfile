################################################################################  
# #  
# {o,o} #  
# |)__) #  
# -"-"- #  
# #  
################################################################################  
#  
# Price pilot's projectbuilder  
#  
##################################---BASE---####################################  
  
FROM pricepilotio/base  
  
################################################################################  
  
################################---MAINTAINER---################################  
  
MAINTAINER Price pilot <hello@pricepilot.io>  
  
################################################################################  
  
###################################---BUILD---##################################  
  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -; \  
apt-get update; \  
apt-get install -q -y \  
git \  
curl \  
wget \  
build-essential \  
make \  
nodejs \  
python2.7 \  
libcurl4-openssl-dev; \  
apt-get clean  
  
RUN npm install -g \  
bower \  
grunt \  
grunt-cli \  
gulp \  
phantomjs-prebuilt \  
load-grunt-tasks \  
time-grunt \  
raml2html  
  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
  
################################################################################  
#################################---COMMAND---##################################  
  
CMD true  
################################################################################  

