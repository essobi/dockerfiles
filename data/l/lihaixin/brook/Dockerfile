# USE for client down  
FROM nginx:stable-alpine  
WORKDIR /usr/share/nginx/html/  
  
#RUN brook_new_ver=`wget -qO- https://github.com/txthinking/brook/tags| grep
"/txthinking/brook/releases/tag/"| head -n 1| awk -F "/tag/" '{print $2}'| sed
's/\">//'` && \  
ENV VERSION v20180401  
ENV HTTPDIR /usr/share/nginx/html/  
  
  
  
#Down client file  
# RUN wget --no-check-certificate -O ${HTTPDIR}/brook.exe
"https://github.com/txthinking/brook/releases/download/${VERSION}/brook.exe"  
# wget --no-check-certificate -O ${HTTPDIR}/Brook.white.exe
"https://github.com/txthinking/brook/releases/download/${VERSION}/Brook.white.exe"
&& \  
# wget --no-check-certificate -O ${HTTPDIR}/Brook.386.exe
"https://github.com/txthinking/brook/releases/download/${VERSION}/Brook.386.exe"
&& \  
# wget --no-check-certificate -O ${HTTPDIR}/Brook.386.white.exe
"https://github.com/txthinking/brook/releases/download/${VERSION}/Brook.386.white.exe"
&& \  
# wget --no-check-certificate -O ${HTTPDIR}/Brook.apk
"https://github.com/txthinking/brook/releases/download/${VERSION}/Brook.apk"  
ADD
https://github.com/txthinking/brook/releases/download/${VERSION}/Brook.Setup.exe
${HTTPDIR}  
ADD https://github.com/txthinking/brook/releases/download/${VERSION}/Brook.apk
${HTTPDIR}  
ADD https://github.com/txthinking/brook/releases/download/${VERSION}/Brook.dmg
${HTTPDIR}  
ADD https://docs.google.com/document/export?format=pdf&id=1KrYAvh-
RHhaKTHELOFEJO5c7H0dHkzU3AeALRxvC7zE ${HTTPDIR}  
ADD ./index.html /usr/share/nginx/html/  
RUN mv export brook使用指南.pdf && chmod 644 ./*  
  
CMD ["nginx", "-g", "daemon off;"]  

