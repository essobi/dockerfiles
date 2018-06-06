FROM rocker/r-base  
MAINTAINER "Pradeep Bashyal" pbashyal@nmdp.org  
  
# Install apache and Cairo dependencies required by FastRWeb  
RUN apt-get update \  
&& apt-get install -y apache2 libcairo2-dev libxt-dev \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y  
  
# Install FastRWeb and its dependencies  
RUN install2.r --error \  
Rserve \  
Cairo \  
FastRWeb \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
# Enable the cgi-bin module  
# Change the /cgi-bin/ path to /api/  
RUN a2enmod cgid \  
&& sed -i -e 's/ \/cgi-bin\/ / \/api\/ /' /etc/apache2/conf-enabled/serve-cgi-
bin.conf  
  
# Install FastRWeb init script  
# Set apache as the directory owner  
RUN cd /usr/local/lib/R/site-library/FastRWeb \  
&& sh install.sh \  
&& chown -R www-data:www-data /var/FastRWeb  
  
# Install the R cgi-bin mod  
RUN cp "/usr/local/lib/R/site-library/FastRWeb/cgi-bin/Rcgi" /usr/lib/cgi-
bin/R  
  
# Add the script that starts up the services in the container  
ADD r-webservice-start.sh /usr/bin/  
  
# Access is through default port  
EXPOSE 80  
CMD ["/usr/bin/r-webservice-start.sh"]  
  

