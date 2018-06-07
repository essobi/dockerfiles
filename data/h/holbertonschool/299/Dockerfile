# 0x0F. Python - Network #0  
FROM holbertonschool/ubuntu-1404-python3  
ADD web /etc/init.d/web  
ADD web.py /tmp/web.py  
ADD run.sh /tmp/run.sh  
  
RUN chmod u+x /tmp/web.py  
RUN chmod u+x /tmp/run.sh  
  
# start run!  
CMD ["./tmp/run.sh"]  

