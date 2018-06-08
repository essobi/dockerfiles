FROM fischerman/docker-ttrss  
MAINTAINER Marco van den Oever <marco@flyingpie.nl>  
  
RUN apt-get update && apt-get install -y git  
  
# Clean-GReader theme  
RUN git clone https://github.com/naeramarth7/clean-greader
/var/www/themes/clean-greader  
RUN ln -s /var/www/themes/clean-greader/wrapper.css /var/www/themes/clean-
greader.css  
  
# Feedly theme  
RUN git clone https://github.com/levito/tt-rss-feedly-theme.git
/var/www/themes/feedly-theme  
RUN cp -r /var/www/themes/feedly-theme/* /var/www/themes/  

