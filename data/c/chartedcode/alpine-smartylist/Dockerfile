FROM alpine  
RUN apk add --update --no-cache curl unzip  
RUN curl -o /tmp/smartylist.zip
https://s3.amazonaws.com/static.smartystreets.com/ListProcessing/smartylist/smartylist_linux-386_latest.zip  
RUN unzip /tmp/smartylist.zip smartylist -d /bin  
RUN rm /tmp/smartylist.zip  
RUN smartylist -version  
RUN apk --purge del curl unzip  
WORKDIR /tmp/share  
CMD smartylist --help  

