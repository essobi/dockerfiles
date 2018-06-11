FROM willhallonline/phpcs:2.9  
MAINTAINER Will Hall "will@willhallonline.co.uk"  
# Retrieve WordPress Coding Standards  
RUN git clone -b master https://github.com/WordPress-Coding-
Standards/WordPress-Coding-Standards.git /root/wpcs  
  
# Set WordPress as default CodeSniffer Standard  
RUN phpcs --config-set installed_paths /root/wpcs  
RUN phpcs --config-set default_standard WordPress  
  
WORKDIR /app  
  
CMD ["phpcs"]  
CMD ["phpcbf"]  

