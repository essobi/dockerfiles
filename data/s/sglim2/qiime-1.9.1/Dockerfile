FROM sglim2/python2-2.7.11  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Software: qiime  
# Software Version: 1.9.1  
# Software Website: https://github.com/biocore/qiime  
# Description: qiime  
##############################################################  
  
ENV APP_NAME=qiime  
ENV VERSION=1.9.1  
  
RUN PATH=/usr/bin PYTHONPATH='' yum install -y libpng-devel freetype-devel ; \  
pip install numpy ; \  
pip install qiime==1.9.1  
CMD ["/bin/bash"]  
  

