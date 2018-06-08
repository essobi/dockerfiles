FROM palshife/ssh  
RUN apt-get update && apt-get install -y gnucash ofx aqbanking-tools libdbd-
mysql  
RUN useradd -m -s /usr/bin/gnucash gnucash && echo 'gnucash:gnucash' |
chpasswd  
EXPOSE 22  
ENTRYPOINT ["/usr/bin/svscan", "/etc/myservices/"]  

