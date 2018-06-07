FROM tutum/debian-wheezy  
MAINTAINER Mark Redar mredar@gmail.com  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y -q python  
  
EXPOSE 25  
  
ADD smtpd-run.py /smtpd-run.py  
  
# smtpd-run.py uses smtpd std lib server running in asyncore  
CMD python /smtpd-run.py  

