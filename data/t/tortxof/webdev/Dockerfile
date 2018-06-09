FROM tortxof/ruby-node  
LABEL maintainer="Daniel Jones <tortxof@gmail.com>"  
  
RUN curl -L \  
https://github.com/zyedidia/micro/releases/download/v1.4.0/micro-1.4.0-linux64.tar.gz
\  
| tar -xzOf - micro-1.4.0/micro \  
> /usr/local/bin/micro && \  
chmod +rx /usr/local/bin/micro  
  
RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh  
  
RUN wget -qO /usr/local/bin/stout
https://github.com/cloudflare/Stout/releases/download/v1.3.2/stout-linux && \  
chmod +x /usr/local/bin/stout  
  
RUN apt-get update && \  
apt-get install -y \  
apt-transport-https \  
ca-certificates \  
sudo \  
groff \  
less  
  
ENV CLOUDSDK_PYTHON=/usr/bin/python2  
ENV CLOUD_SDK_REPO=cloud-sdk-jessie  
RUN echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" |
tee -a /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
  
RUN apt-get update && \  
apt-get install -y \  
google-cloud-sdk \  
kubectl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install \  
awscli \  
pipenv  
  
RUN gem install -f \  
bundler \  
jekyll \  
therubyracer \  
sass \  
susy \  
compass \  
breakpoint \  
mustache \  
bourbon \  
neat  
  
RUN yarn global add \  
eslint \  
prettier \  
nodemon \  
babel-cli \  
grunt \  
gulp \  
browser-sync \  
autoprefixer-cli \  
foundation-cli \  
ember-cli \  
express-generator \  
http-server \  
harp \  
brunch \  
create-react-app \  
vue-cli \  
surge \  
serverless \  
claudia  
  
ENV SHELL=/bin/bash  
  
ENV TERM=linux  
  
ENV HOME=/host  
  
VOLUME ["/host"]  
  
WORKDIR /host  
  
CMD ["/bin/bash"]  

