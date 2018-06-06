FROM nginx  
  
MAINTAINER Matt Kunkel matt@mrkunkel.com  
  
RUN apt-get update && \  
apt-get install -y \  
git && \  
rm -rf /usr/share/nginx/html/* && \  
git clone https://github.com/modulusx/mrkunkel-resume.git
/usr/share/nginx/html/ && \  
apt-get remove --auto-remove -y \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

