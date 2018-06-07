FROM johnnyzheng/centos-nginx-php  
MAINTAINER Johnny Zheng <johnny@itfolks.com.au>  
  
RUN PRESTASHOPINSTALL=prestashop-install && \  
cd / && \  
rm -rf $PRESTASHOPINSTALL && \  
curl -o $PRESTASHOPINSTALL.zip
http://www.prestashop.com/download/old/prestashop_1.6.0.9.zip && \  
unzip $PRESTASHOPINSTALL.zip && \  
rm -f $PRESTASHOPINSTALL.zip  
# cd /$PRESTASHOPINSTALL && \  
# mv install-dev install && \  
# mv admin-dev admin && \  
# rm -rf .git  
# git clone https://github.com/PrestaShop/PrestaShop.git $PRESTASHOPINSTALL &&
\  
# Exposed ENV  
ENV DOMAIN **prestashop**  
ENV SHOP_NAME **prestashop**  
ENV LANGUAGE Asia/Shanghai  
ENV SHOP_PASSWORD 0123456789  
ENV SHOP_EMAIL pub@prestashop.com  
ENV OVERRIDDEN FALSE  
  
ADD container-files /  

