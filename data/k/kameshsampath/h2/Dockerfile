FROM kameshsampath/jpm4j  
  
MAINTAINER Kamesh Sampath, kamesh.sampath@hotmail.com  
  
ENV WEB_PORT=8082  
RUN jpm install --name h2 com.h2database:h2@1.4.192  
  
EXPOSE $WEB_PORT  
  
CMD h2 -web -webAllowOthers -tcp -webPort $WEB_PORT

