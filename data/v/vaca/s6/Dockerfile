FROM vaca/alpine  
  
RUN ["apk", "--no-cache", "add", "s6", "s6-portable-utils"]  
COPY ["over", "/"]  
  
CMD ["init"]  

