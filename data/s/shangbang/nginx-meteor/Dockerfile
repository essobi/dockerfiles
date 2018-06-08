FROM nginx:1.9.12  
  
MAINTAINER Michael Shang  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
git \  
vim \  
supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV METEOR_RELEASE 1.4.2.3  
  
RUN curl https://install.meteor.com/ 2>/dev/null | sed 's/^RELEASE/#RELEASE/'|
RELEASE=$METEOR_RELEASE sh  
  
RUN ln -s ~/.meteor/packages/meteor-tool/*/mt-
os.linux.x86_64/dev_bundle/bin/node /usr/bin/ && \  
ln -s ~/.meteor/packages/meteor-tool/*/mt-os.linux.x86_64/dev_bundle/bin/npm
/usr/bin/ && \  
rm /etc/nginx/conf.d/default.conf  
  
ENV PORT 3000  

