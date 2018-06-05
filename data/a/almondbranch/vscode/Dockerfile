FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y binutils  
  
# Install node.js v6 so that uglified regexes formats match (see
https://github.com/mishoo/UglifyJS2/issues/1929)  
RUN cd ~ && \  
apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh && \  
bash nodesource_setup.sh && \  
apt-get install -y nodejs build-essential  
  
# Install other dependencies  
RUN apt-get install -y make g++ libx11-dev libxkbfile-dev fakeroot  
  
# Download the vscode source repo  
RUN cd /home && \  
apt-get install -y git && \  
git clone https://github.com/microsoft/vscode  
  
# Install Python  
RUN apt-get install -y python2.7 python-pip && \  
pip install --upgrade pip && \  
pip install GitPython  
  
# Install other needed dependencies  
RUN apt-get install -y libnss3 libgtk2.0-0 libxtst6 libxss1 libgconf-2-4
libasound2 libcanberra-gtk-module  
  
# Add the release icon and product.json to the container (Don't update
package.json because this will cause the question mark icon to appear)  
RUN mkdir /tmp/release_vscode_items  
ADD code.png /tmp/release_vscode_items/code.png  
ADD product_v1.12.2.json /tmp/release_vscode_items/product.json  
  
# Set the working directory of the vscode git repo to match the commit
mentioned in the distribution product.json file that was added from the
release version  
ADD product_parser.py /home/product_parser.py  
RUN cd /home/vscode && \  
python /home/product_parser.py
--product_json='/tmp/release_vscode_items/product.json'
\--vscode_repo='/home/vscode'  
  
# Move the release icon and product.json into the source code  
RUN rm /home/vscode/resources/linux/code.png && \  
cp /tmp/release_vscode_items/code.png /home/vscode/resources/linux && \  
rm /home/vscode/product.json && \  
cp /tmp/release_vscode_items/product.json /home/vscode  
  
# Remove vscode release checksums since this docker image will package the app
differently  
ADD checksum_remover.py /tmp  
RUN python /tmp/checksum_remover.py --product_json='/home/vscode/product.json'  
  
# Run the install scripts  
RUN cd /home/vscode && \  
/home/vscode/scripts/npm.sh run-script preinstall && \  
/home/vscode/scripts/npm.sh install --arch=x64 && \  
/home/vscode/scripts/npm.sh run-script postinstall  
  
# For some reason postinstall misses some npm install calls, fix those  
RUN cd /home/vscode/extensions/css/server && /home/vscode/scripts/npm.sh
install && \  
cd /home/vscode/extensions/vscode-colorize-tests &&
/home/vscode/scripts/npm.sh install && \  
cd /home/vscode/extensions/vscode-colorize-tests &&
/home/vscode/scripts/npm.sh run-script postinstall && \  
cd /home/vscode/extensions/json/server && /home/vscode/scripts/npm.sh install
&& \  
cd /home/vscode/extensions/html/server && /home/vscode/scripts/npm.sh install  
  
# Build, compile, optimize and minify (must create mac resource for this to
work which is unfortunate...)  
RUN npm install -g gulp && \  
touch /home/vscode/resources/darwin/Credits.rtf && \  
cd /home/vscode && gulp vscode-linux-x64-min  
  
# Download the distributable version of electron specified in package.json  
RUN npm install -g electron-download && \  
mkdir /tmp/electron-downloads && \  
ELECTRON_VERSION=$( \  
cat /home/vscode/package.json | \  
grep electronVersion | \  
sed -e
's/[[:space:]]*"electronVersion":[[:space:]]*"\\([0-9.]*\\)"\\(,\\)*/\1/' \  
) && \  
electron-download --version=$ELECTRON_VERSION \--platform=linux --arch=x64
--cache=/tmp/electron-downloads  
  
# Install X11  
RUN apt-get install -y sudo x11-apps libx11-xcb-dev  
  
# Set up permissions for X11 access.  
# Replace 1000 with your user / group id.  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer  
  
USER developer  
  
# Create directories for the config and extensions so that they can be mapped
to volumes when running  
RUN mkdir -p /home/developer/.config/code-oss-dev &&\  
mkdir /home/developer/extensions_vscode  
  
# Unzip the distributable version of electron  
RUN sudo apt-get install -y unzip && \  
mkdir -p /home/developer/vscode_final/resources/app/out && \  
unzip '/tmp/electron-downloads/*.zip' -d /home/developer/vscode_final  
  
# Place the built version of vscode next to the distributable version of
electron  
RUN rm /home/developer/vscode_final/resources/default_app.asar && \  
cp -r /home/vscode/out-vscode-min/.
/home/developer/vscode_final/resources/app/out && \  
cd /home/vscode && \  
cp -r LICENSE.txt ThirdPartyNotices.txt extensions node_modules package.json
product.json resources /home/developer/vscode_final/resources/app  
  
# Run vscode!!  
CMD ./home/developer/vscode_final/electron --extensions-
dir=/home/developer/extensions_vscode  

