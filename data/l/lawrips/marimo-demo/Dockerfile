FROM node:4-onbuild  
ENV "marimo:port" "10001"  
ENV "monitoring:defaultTest" "echo,simple,wikipedia"  
ENV "monitoring:env:wikipedia" "wikipediaEnv"  
ENV "monitoring:env:simple" "simpleEnv"  
ENV "monitoring:delay" "1000"  
ENV "webserver:port" "10000"  
ENV "DEBUG" "marimo"  
EXPOSE 10000  
EXPOSE 10001  
CMD ["node", "server.js"]  

