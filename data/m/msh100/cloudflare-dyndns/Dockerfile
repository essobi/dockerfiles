FROM ubuntu  
MAINTAINER Marcus Hughes <hello@msh100.uk>  
  
# Update apt and install php-cli  
RUN apt-get update  
RUN apt-get install -y php5-cli  
  
# Add cloudflare api script  
ADD updateip /  
RUN chmod +x updateip  
  
CMD ["/updateip"]

