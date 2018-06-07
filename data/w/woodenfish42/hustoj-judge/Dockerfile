FROM woodenfish42/hustoj-judge:base  
LABEL maintainer="muzea <mr.muzea@gmail.com>"  
  
COPY judge_client.patch /  
  
RUN set -ex \  
&& apt update \  
&& apt install -y \  
pypy \  
&& cd /hustoj/trunk/core/judged \  
&& make \  
&& chmod +x judged \  
&& cp judged /usr/bin \  
&& cd ../judge_client \  
&& patch --ignore-whitespace judge_client.cc /judge_client.patch \  
&& make \  
&& chmod +x judge_client \  
&& cp judge_client /usr/bin \  
&& rm -rf /hustoj  
  
WORKDIR /home/judge  
  
CMD judged && tail -f /dev/null  
  

