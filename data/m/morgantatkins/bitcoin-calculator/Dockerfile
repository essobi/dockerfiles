FROM bash  
RUN apk --no-cache add curl jq bc  
ADD https://raw.githubusercontent.com/MorganTAtkins/crypto-
utilities/master/mBTC_Converter.sh /crypto-converter/mBTC_Converter.sh  
RUN chmod +x /crypto-converter/mBTC_Converter.sh  
ENTRYPOINT [ "/bin/ash", "/crypto-converter/mBTC_Converter.sh" ]  

