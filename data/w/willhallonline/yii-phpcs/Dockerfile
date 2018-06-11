FROM willhallonline/phpcs:2.9  
MAINTAINER Will Hall "will@willhallonline.co.uk"  
# Retrieve Yii2 Coding Standards  
RUN git clone -b master git://github.com/yiisoft/yii2-coding-standards.git
/root/yii-phpcs  
  
# Set Yii2 as default CodeSniffer Standard  
RUN phpcs --config-set installed_paths /root/yii-phpcs  
RUN phpcs --config-set default_standard Yii2  
  
WORKDIR /app  
  
CMD ["phpcs"]  
CMD ["phpcbf"]  

