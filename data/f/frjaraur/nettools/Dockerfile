FROM loadimpact/k6 as k6  
FROM frjaraur/nettools:small  
USER 65500  
CMD ["/help"]  
COPY \--from=k6 /root/k6 /usr/local/bin  
COPY \--from=k6 /etc/ssl /etc/ssl  

