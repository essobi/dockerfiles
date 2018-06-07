FROM azukiapp/alpine:3.3  
MAINTAINER Hugo Courtecuisse <hugo.courtecuisse@gmail.com>  
  
# Create new folder  
RUN mkdir /tmp/zdsfront  
WORKDIR /tmp/zdsfront  
  
# Add python dependency  
RUN wget -O python2.7-static
https://raw.githubusercontent.com/pts/staticpython/master/release/stackless2.7-static
&& mv python2.7-static /bin/python && chmod +x /bin/python  
  
# Install needed package  
RUN apk add --no-cache nodejs make g++ nasm autoconf automake gettext zlib-dev  
  
# Build front  
RUN wget https://raw.githubusercontent.com/zestedesavoir/zds-
site/dev/package.json && \  
npm install -g npm && \  
npm install  
  
# When root login, we need to copy the folder node_modules  
RUN printf "%s\n" "if [ ! -d /code/node_modules/ ]; then" "mkdir
/code/node_modules/" "cd /code/" "mount -o bind /tmp/zdsfront/node_modules/
node_modules/" "fi" "cd /code/ && npm run gulp build" > /root/.bashrc && chmod
+x /root/.bashrc  

