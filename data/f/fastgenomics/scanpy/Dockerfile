FROM alpine:3.7  
# add additional mirror  
RUN echo http://mirror1.hs-esslingen.de/pub/Mirrors/alpine/v3.7/main >>
/etc/apk/repositories; \  
echo http://mirror1.hs-esslingen.de/pub/Mirrors/alpine/v3.7/community >>
/etc/apk/repositories  
  
COPY requirements.txt /requirements/  
COPY build.sh /  
  
# bash is needed to run the script  
RUN apk add --no-cache bash && bash build.sh && rm build.sh  

