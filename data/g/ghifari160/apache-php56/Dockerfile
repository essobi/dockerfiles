FROM ghifari160/apache:16.04  
MAINTAINER Ghifari160 <ghifari160@ghifari160.com>  
  
# Disable interactive functions  
ENV DEBIAN_FRONTEND noninteractive  
  
# Switch locale to UTF-8 and add ppa for php56  
RUN export LC_ALL=en_US.UTF-8 && add-apt-repository -y ppa:ondrej/php  
  
# Add the custom default page  
RUN rm /var/www/html/index.html  
ADD index.php /var/www/html/index.php  
  
# Install php56  
RUN apt update && apt install -y php5.6 php5.6-mysql php-gettext \  
php5.6-mbstring php-xdebug libapache2-mod-php5.6 php5.6-dom  
  
# Cleanup after apt  
RUN rm -rf /var/lib/apt/lists/*  

