FROM python:2.7.11-alpine  
  
MAINTAINER Fabio Corneti <info@corneti.com>  
  
ENV DELAY 5  
ENV NEXT_ACTION_LABEL next_action  
ENV INBOX_METHOD parallel  
ENV PARALLEL_SUFFIX .  
ENV SERIAL_SUFFIX _  
ENV HIDE_FUTURE 7  
ENV EXTRA_ARGS ""  
RUN apk update && apk add git && \  
pip install git+https://github.com/nikdoof/NextAction@support/0.3 && \  
rm -rf /var/cache/apk/* && \  
apk del git  
  
CMD ["sh","-c","nextaction -a ${TODOIST_APIKEY} -l ${NEXT_ACTION_LABEL} -d
$DELAY \--inbox=$INBOX_METHOD \--parallel_suffix=$PARALLEL_SUFFIX
\--serial_suffix=$SERIAL_SUFFIX \--hide_future=$HIDE_FUTURE $EXTRA_ARGS"]  

