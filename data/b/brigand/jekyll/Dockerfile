FROM brigand/ruby  
RUN apk update \  
&& apk add ruby-dev libpq libgcc ca-certificates make gcc libc-dev libffi-dev
\  
nodejs 'python<3' zlib-dev libxml2 libxml2-dev libxslt libxslt-dev \  
&& gem install nokogiri -- --use-system-libraries -N \  
&& gem install jekyll -N \  
&& gem install github-pages -N \  
&& apk del --purge ruby-dev \  
libgcc gcc make libc-dev libffi-dev zlib-dev libxml2-dev libxslt-dev \  
&& apk add ruby-json  
RUN mkdir /usr/ws  
WORKDIR /usr/ws  
CMD ["echo", "This container has no default action."]  
  

