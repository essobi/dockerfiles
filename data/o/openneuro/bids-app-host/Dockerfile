FROM docker:17.05.0-ce  
  
RUN apk add --no-cache --update bash jq curl util-linux && \  
mkdir /snapshot && \  
mkdir /output  
  
COPY run-bids-app.sh /usr/local/bin/run-bids-app.sh  
  
CMD /usr/local/bin/run-bids-app.sh  

