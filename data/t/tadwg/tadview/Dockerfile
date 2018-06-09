FROM paijp/centos6-apache-php-sqlite2-pdflib:latest  
  
RUN \  
set -x &&\  
yum -y install php-gd php-mbstring wget  
RUN \  
set -x &&\  
cd /var/www/html/ &&\  
mkdir -p fonts &&\  
cd fonts &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/ipag.ttf' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/ipagp.ttf' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/ipam.ttf' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/ipamp.ttf' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT01.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT02.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT03.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT04.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT05.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT06.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT07.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT08.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT09.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT10.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT11.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT12.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TGothic-GT13.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT01.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT02.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT03.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT04.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT05.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT06.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT07.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT08.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT09.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT10.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT11.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT12.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TKaisho-GT13.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT01.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT02.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT03.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT04.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT05.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT06.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT07.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT08.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT09.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT10.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT11.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT12.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/TMincho-GT13.ttc' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/koganei.ttf'  
RUN \  
set -x &&\  
cd /var/www/html/ &&\  
wget
'https://github.com/tadwg/tadview/raw/master/zend/ZendFramework-1.12.18-minimal.tar.gz'
&&\  
tar xfz ZendFramework-1.12.18-minimal.tar.gz &&\  
cd ZendFramework-1.12.18-minimal/library/Zend/Pdf/ &&\  
mv Font.php Font_160624.php &&\  
wget 'https://github.com/tadwg/tadview/raw/master/zend/Pdf/Font.php' &&\  
cd Canvas/ &&\  
mv Abstract.php Abstract_160624.php &&\  
wget
'https://github.com/tadwg/tadview/raw/master/zend/Pdf/Canvas/Abstract.php' &&\  
cd ../Resource/ &&\  
mv Font.php Font_160624.php &&\  
wget 'https://github.com/tadwg/tadview/raw/master/zend/Pdf/Resource/Font.php'
&&\  
cd Font/ &&\  
mv CidFont.php CidFont_160624.php &&\  
wget
'https://github.com/tadwg/tadview/raw/master/zend/Pdf/Resource/Font/CidFont.php'  
  
RUN \  
set -x &&\  
ldconfig /usr/local/lib &&\  
cd /var/www/html/ &&\  
wget 'https://github.com/tadwg/tadview/raw/master/index.html' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/ath.txt' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/env.php' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/envl.php' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/tadview.php' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/tadviewbp.php' &&\  
wget 'https://github.com/tadwg/tadview/raw/master/tcmap.php' &&\  
cd fonts &&\  
wget 'https://github.com/tadwg/tadview/raw/master/fonts/tcmap.sq2'  
  
EXPOSE 80 443  
CMD apachectl start&&tail -f /var/log/httpd/access_log  

