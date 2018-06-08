FROM ruby:2.2.3  
ENV TZ Asia/Tokyo  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
mysql-client-5.5 \  
\  
&& rm -rf /var/lib/apt/lists/*  
  
# Setup node  
ENV NODE_VERSION=8.x  
RUN curl -sL https://deb.nodesource.com/setup_$NODE_VERSION | bash \  
&& apt-get install -y nodejs  
  
# Setup yarn  
ENV PATH /root/.yarn/bin:$PATH  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash  

