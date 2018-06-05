FROM progrium/cedarish:cedar14  
  
RUN curl
https://github.com/gliderlabs/herokuish/releases/download/v0.3.33/herokuish_0.3.33_linux_x86_64.tgz
\  
\--silent -L | tar -xzC /bin  
  
# install herokuish supported buildpacks and entrypoints  
RUN /bin/herokuish buildpack install \  
&& ln -s /bin/herokuish /build \  
&& ln -s /bin/herokuish /start \  
&& ln -s /bin/herokuish /exec  
  
# backwards compatibility  
ADD ./rootfs /  
  
# From tutum/buildstep  
ADD run.sh /run.sh  
RUN rm -fr /app  
  
ONBUILD ADD . /app  
ONBUILD RUN /build/builder  
  
ENTRYPOINT ["/run.sh"]  

