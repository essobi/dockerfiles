FROM vimagick/scrapyd  
  
ADD ./*.txt /etc/scrapyd/  
RUN cd /etc/scrapyd; \  
# apt-get -y update; \  
# apt-get -y upgrade; \  
# apt-get -y install $(grep -vE "^\s*#" packages.txt | tr "\n" " "); \  
pip install -r requirements.txt;  

