FROM moonshotinternet/base-image:003  
LABEL vendor=Moonshot-Internet  
LABEL com.moonshot.name=ci-scripts  
LABEL com.moonshot.version=1.0.0  
  
# install libs  
RUN apk add --no-cache \  
build-base \  
python3-dev  
  
# run extra install scripts  
COPY ./docker /tmp/install  
RUN find /tmp/install -type f -name 'install*.sh' -exec sh -e {} \; \  
&& rm -fr /tmp/*  
  
# add scripts  
COPY ./src/ /root/bin  
# flatten scripts, clean-up dirs, add execution flag to binaries, link'em to
the bin PATH  
RUN find /root/bin -type f -exec sh -c 'mv "$@" /root/bin' _ {} + \  
&& find /root/bin/* -type d -depth -exec rmdir {} + \  
&& chmod +x /root/bin/*.sh \  
&& ln -s /root/bin/*.sh /usr/local/bin/.  
  
# add ansible playbooks  
COPY ./ansible /ansible  

