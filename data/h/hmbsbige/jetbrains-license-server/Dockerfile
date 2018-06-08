FROM alpine  
ENV l 0.0.0.0  
ADD Server_linux_amd64 /usr/local/bin/  
RUN chmod a+x /usr/local/bin/Server_linux_amd64  
CMD ["sh", "-c", "/usr/local/bin/Server_linux_amd64 -p 2233 -u HMBSbige -l $l
-prolongationPeriod 999999999999"]  
EXPOSE 2233

