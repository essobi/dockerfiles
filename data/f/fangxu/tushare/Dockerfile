# 搭建 tushare 环境  
FROM alpine  
  
LABEL maintainer="fangxu <fangxu1999@126.com>"  
RUN apk update && apk upgrade \  
&& apk add python3-dev \  
&& apk add musl-dev \  
&& apk add libxslt-dev \  
&& apk add gcc \  
&& apk add g++ \  
&& pip3 install lxml \  
&& pip3 install pandas \  
&& pip3 install requests \  
&& pip3 install bs4 \  
&& pip3 install tushare \  
&& apk add python3 \  
&& apk add libxslt \  
&& apk del gcc g++ python3-dev musl-dev libxslt-dev  

