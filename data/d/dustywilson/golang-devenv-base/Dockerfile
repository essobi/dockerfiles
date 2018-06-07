FROM ubuntu:latest  
  
# install all packages  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
apt-transport-https \  
autoconf \  
automake \  
bash-completion \  
bzr \  
ca-certificates \  
curl \  
g++ \  
gconf2 \  
gconf-service \  
git \  
gvfs-bin \  
fakeroot \  
inotify-tools \  
iputils-ping \  
libasound2 \  
libcap2 \  
libgconf-2-4 \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libtool \  
libx11-xcb1 \  
libxkbfile1 \  
libxss1 \  
libxtst6 \  
lsb-release \  
make \  
nano \  
python \  
ssh \  
telnet \  
unzip \  
vim \  
xdg-utils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# install protobuf  
RUN git clone https://github.com/google/protobuf.git /tmp/protobuf && \  
cd /tmp/protobuf && \  
./autogen.sh && \  
./configure && \  
make && \  
make check && \  
make install && \  
ldconfig && \  
cd / && \  
rm -Rf /tmp/protobuf  
  
# install Google Cloud SDK and Kubernetes (kubectl, helm)  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
&& \  
echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c -s)
main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
google-cloud-sdk \  
kubectl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN curl $(curl -L https://github.com/kubernetes/helm/releases/latest | grep
-E 'href="https://.*-linux-amd64.tar.gz"' | cut -d'"' -f2) | tar -zxOf- linux-
amd64/helm > /usr/bin/helm && \  
chmod 755 /usr/bin/helm  
  
# install Actions on Google CLI  
RUN curl
https://dl.google.com/gactions/updates/bin/linux/amd64/gactions/gactions >
/usr/bin/gactions && \  
chmod 755 /usr/bin/gactions  
  
# install Google Cloud Fonts  
RUN curl -L https://github.com/google/fonts/archive/master.zip > /tmp/google-
cloud-fonts.zip && \  
mkdir -p /usr/share/fonts/google-cloud-fonts && \  
unzip -qd /usr/share/fonts/google-cloud-fonts/ /tmp/google-cloud-fonts.zip &&
\  
rm /tmp/google-cloud-fonts.zip && \  
fc-cache -f  
  
# install Go font  
RUN git clone https://go.googlesource.com/image /tmp/go-image && \  
mkdir -p /usr/share/fonts/gofont && \  
cp /tmp/go-image/font/gofont/ttfs/*.ttf /usr/share/fonts/gofont/ && \  
rm -Rf /tmp/go-image && \  
fc-cache -f  
  
# install FiraCode font  
RUN git clone https://github.com/tonsky/FiraCode.git /tmp/firacode && \  
mkdir -p /usr/share/fonts/firacode && \  
cp /tmp/firacode/distr/ttf/*.ttf /usr/share/fonts/firacode/ && \  
rm -Rf /tmp/firacode && \  
fc-cache -f  
  
# install MongoDB client  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-3.4.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
mongodb-org-shell \  
mongodb-org-mongos \  
mongodb-org-tools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# install nodejs  
ENV NODEREPO=node_6.x  
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- && \  
echo "deb https://deb.nodesource.com/$NODEREPO $(lsb_release -c -s) main" >
/etc/apt/sources.list.d/nodesource.list && \  
echo "deb-src https://deb.nodesource.com/$NODEREPO $(lsb_release -c -s) main"
>> /etc/apt/sources.list.d/nodesource.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# setup user  
RUN useradd -d /user -m user  
WORKDIR /user  
USER user  
# configure npm  
RUN mkdir /user/.npm-global && \  
npm config set prefix /user/.npm-global && \  
echo 'PATH="$PATH:/user/.npm-global/bin"'>> /user/.profile  
  
# install yarn, bower, polymer, firebase, localtunnel  
RUN npm install --global bower  
RUN npm install --global yarn  
RUN npm install --global localtunnel  
RUN npm install --global polymer-cli  
RUN npm install --global firebase-tools  
  
# add {kubectl,helm} autocomplete  
RUN echo "source <("kubectl" completion bash); source <("helm" completion
bash)" >> /user/.bashrc  
  
# install Google App Engine SDK  
RUN gsutil cp gs://appengine-sdks/featured/$(curl
https://cloud.google.com/appengine/docs/standard/go/download 2>/dev/null |
grep \"go_appengine_sdk_linux_amd64- | cut -d\" -f2 | head -n1)
/tmp/appengine.zip && \  
unzip /tmp/appengine.zip && \  
rm /tmp/appengine.zip  
  
# setup exec  
ENTRYPOINT ["/bin/bash", "-c", "echo 'This is intended as a base layer, not to
be used directly.'"]  

