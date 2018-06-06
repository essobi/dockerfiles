FROM piratenbpt/base  
RUN apt-get install -y cups cups-pdf  
RUN apt-get install -y cups-driver-gutenprint  
  
# Disbale some cups backend that are unusable within a container  
RUN mv /usr/lib/cups/backend/parallel /usr/lib/cups/backend-available/ &&\  
mv /usr/lib/cups/backend/serial /usr/lib/cups/backend-available/ &&\  
mv /usr/lib/cups/backend/usb /usr/lib/cups/backend-available/  
  
ADD cupsd.conf /etc/cups/cupsd.conf  
ADD startup.sh /startup.sh  
EXPOSE 631  
ENV USERNAME admin  
ENV PASSWORD secret  
CMD /startup.sh  

