#http://qiita.com/hnakamur/items/0b72590136cece29faee  
FROM typista/base  
#FROM typista/base:0.5  
RUN wget https://raw.githubusercontent.com/typista/docker-
xmail/master/files/entrypoint.sh -O /etc/entrypoint.sh && \  
chmod +x /etc/entrypoint.sh && \  
yum update -y && \  
wget http://www.xmailserver.org/xmail-1.27.tar.gz && \  
tar xvzf xmail-1.27.tar.gz && \  
cd xmail-1.27;make -f Makefile.lnx && \  
cp -r MailRoot /var/ && \  
cp sendmail.sh /var/MailRoot/ && \  
chmod +x /var/MailRoot/sendmail.sh && \  
mv /usr/sbin/sendmail{,.org} && \  
ln -s /var/MailRoot/sendmail.sh /usr/sbin/sendmail && \  
ls bin/ | grep -v ".o" | xargs -I{} cp bin/{} /var/MailRoot/bin/ && \  
chmod 700 /var/MailRoot/  

