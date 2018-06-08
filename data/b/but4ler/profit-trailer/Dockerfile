FROM openjdk:8-jre-alpine  
  
#ENV PATH /usr/local/bin:$PATH  
ARG PT_VERSION=${PT_VERSION:-2.0.12}  
ENV PT_VERSION ${PT_VERSION}  
  
# install tools  
RUN apk add --update wget bash  
  
#ENV PT_DL=https://github.com/taniman/profit-
trailer/releases/download/$PT_VERSION/ProfitTrailer-$PT_VERSION.zip  
RUN wget https://github.com/taniman/profit-
trailer/releases/download/$PT_VERSION/ProfitTrailer-$PT_VERSION.zip -P /opt  
#ADD $PT_DL /opt  
COPY entrypoint.sh /  
  
VOLUME ["/app/ProfitTrailer"]  
  
CMD ["/entrypoint.sh"]  
  
EXPOSE 8081  

