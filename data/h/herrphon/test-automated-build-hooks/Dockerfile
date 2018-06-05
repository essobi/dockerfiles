FROM ubuntu  
  
ARG BUILD_DATE  
ARG GIT_SHA1  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.git-sha1=$GIT_SHA1  
  
ADD pwd_file /  
ADD build.files /  
ADD build.env /  
  
RUN echo ${BUILD_DATE} > blubb \  
&& echo ${GIT_SHA1} >> blubb  
  
CMD ["cat", "blubb"]  
  

