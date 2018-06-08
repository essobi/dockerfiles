FROM alpine  
LABEL maintainer="Gildas Cherruel <gildas@breizh.org>"  
LABEL version="0.0.2"  
LABEL description="Runs jq, the JSON processor"  
  
RUN addgroup -S jq && \  
adduser -S -g jq jq  
  
RUN apk add --no-cache jq  
  
USER jq  
  
ENTRYPOINT [ "jq", "-C" ]  
CMD [ "" ]  

