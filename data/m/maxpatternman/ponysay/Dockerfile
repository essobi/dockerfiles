FROM alpine:3.7  
RUN apk add --no-cache git \  
python3 \  
gzip \  
texinfo \  
&& git clone https://github.com/erkin/ponysay.git \  
&& cd /ponysay \  
&& python3 setup.py --freedom=partial install \  
&& apk del git \  
gzip \  
texinfo \  
&& rm -r -f /ponysay  
  
LABEL maintainer="Max Patternman (https://github.com/maxpatternman)"  
  
CMD ["ponysay", "--help"]  

