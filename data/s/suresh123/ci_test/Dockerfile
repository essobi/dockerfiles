#  
# Version 0.1.0  
FROM ubuntu:14.04  
RUN mkdir /home/TTU  
ADD sourcefile.sh /home/TTU/sourcefile.sh  
ADD test_script.sh /home/TTU/test_script.sh  
RUN chmod 777 /home/TTU/sourcefile.sh  
RUN sh /home/TTU/sourcefile.sh  
RUN chmod 777 /home/TTU/test_script.sh  
RUN touch /home/TTU/logfile.log  
RUN sh /home/TTU/test_script.sh >> /home/TTU/logfile.log

