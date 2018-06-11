FROM tutum/wordpress:latest  
MAINTAINER Rudolf Olah <omouse@gmail.com>  
  
# Install curl and unzip  
RUN apt-get install -y curl unzip  
  
# Create uploads directory and setup permission  
RUN mkdir -p /var/www/wp-content/uploads  
RUN chmod 777 /var/www/wp-content/uploads  
  
# Download and unzip plugins  
# Frontend Uploader plugin  
RUN curl http://downloads.wordpress.org/plugin/frontend-uploader.0.7.1.zip >
/var/www/wp-content/plugins/frontend-uploader.zip  
RUN cd /var/www/wp-content/plugins && unzip frontend-uploader.zip  
  
# MailChimp plugin  
RUN curl http://downloads.wordpress.org/plugin/mailchimp-for-wp.1.5.8.zip >
/var/www/wp-content/plugins/mailchimp-for-wp.zip  
RUN cd /var/www/wp-content/plugins && unzip mailchimp-for-wp.zip  
  
# PayPal Donations plugin  
RUN curl http://downloads.wordpress.org/plugin/paypal-donations.1.8.2.zip >
/var/www/wp-content/plugins/paypal-donations.zip  
RUN cd /var/www/wp-content/plugins && unzip paypal-donations.zip  
  
# Jetpack plugin  
RUN curl http://downloads.wordpress.org/plugin/jetpack.2.9.2.zip >
/var/www/wp-content/plugins/jetpack.zip  
RUN cd /var/www/wp-content/plugins && unzip jetpack.zip  
  
# Easy Instagram plugin  
RUN curl http://downloads.wordpress.org/plugin/easy-instagram.3.0.zip >
/var/www/wp-content/plugins/easy-instagram.zip  
RUN cd /var/www/wp-content/plugins && unzip easy-instagram.zip  
  
# Default command  
CMD ["/run.sh"]  

