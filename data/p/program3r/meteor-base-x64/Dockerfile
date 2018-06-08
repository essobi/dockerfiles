FROM program3r/meteor-base-x64:base  
MAINTAINER Joshua Chavez josh@findjosh.com  
WORKDIR /root  
RUN meteor create app  
WORKDIR /root/app  
RUN rm -r app.*  
RUN mkdir packages  
ENV SEC_UPDATES SKIP  
ENV AUTO_APT_ARCHIVE SKIP  
ENV HUB_APIKEY SKIP  
EXPOSE 3000  
VOLUME /root/app  

