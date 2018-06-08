FROM virtuald/nsq:base-0.3.8  
ADD /nsqlookupd.sh /usr/bin/nsqlookupd.sh  
  
EXPOSE 4160  
EXPOSE 4161  
ENTRYPOINT ["/usr/bin/nsqlookupd.sh"]  

