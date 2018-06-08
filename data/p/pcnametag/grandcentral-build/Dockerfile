# Start with this base image  
FROM andmetoo/bitbucket-pipelines-php7:latest  
  
MAINTAINER Ben Yanke <byanke@pcnametag.com>  
  
# Insall needed packages  
RUN add-apt-repository -y ppa:ondrej/php && export
DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y jq
python yamllint python-pip unzip libxml2-dev libldb-dev php7.0-ldap
php7.0-json php7.0-mcrypt php7.0-curl --no-install-recommends && apt-get clean
&& rm -rf /var/lib/apt/lists/*  
# Install node to run webpack (to ensure it compiles) as well as packages
always needed  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install
nodejs && apt-get clean && rm -rf /var/lib/apt/lists/* && npm install
\--global cross-env  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Python Elastic Beanstalk Tooling  
RUN pip install setuptools && pip install wheel && pip install awsebcli  

