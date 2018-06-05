FROM nagucc/gitbook-server  
  
ADD gzlc /gitbook/gzlc  
ADD hr /gitbook/hr  
ADD kb /gitbook/kb  
ADD gzzd /gitbook/gzzd  
ADD Gruntfile.js /gitbook/  
ADD package.json /gitbook/  
ADD README.md /gitbook/  
ADD SUMMARY.md /gitbook/  
ADD zongze.md /gitbook/  
  
WORKDIR /gitbook  
RUN gitbook build  
  
EXPOSE 4000  
WORKDIR /gitbook/_book  
CMD web-server -p 4000  

