FROM znc:latest  
  
# Add Mutter IRC Push Module  
RUN pip3 install requests  
ADD https://bitbucket.org/jmclough/mutter-
push/raw/ce424bd93750209c32fc6a9c8d544f9734b827e3/mutter.py /znc-data/modules/  
ADD https://raw.githubusercontent.com/pR0Ps/znc-logsearch/master/logsearch.py
/znc-data/modules/  

