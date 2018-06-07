FROM debian  
MAINTAINER Mark Redar mredar@gmail.com  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y -q python  
  
EXPOSE 10025  
  
ADD smtpd-run.py /smtpd-run.py  
  
# smtpd-run.py uses smtpd std lib server running in asyncore  
CMD python /smtpd-run.py  

