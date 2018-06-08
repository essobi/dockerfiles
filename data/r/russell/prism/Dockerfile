FROM alpine  
ADD
https://github.com/stoplightio/prism/releases/download/v2.0.0-alpha.7/prism_linux_amd64
/prism  
RUN chmod +x /prism  
EXPOSE 80  
ENTRYPOINT ["/prism", "run", "--mock", "--list", "--spec"]  
CMD ["http://petstore.swagger.io/v2/swagger.json"]  

