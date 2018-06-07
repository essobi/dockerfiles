FROM xataz/nginx-php  
  
MAINTAINER hydrog3n <contact@loicvaille.ovh>  
  
ARG VERSION_SHAARLI=0.9.1  
ARG VERSION_MATERIAL=0.9.0  
ARG VERSION_SHAARLI2TWITTER=1.3.0  
RUN cd /tmp \  
&& wget
https://github.com/shaarli/Shaarli/releases/download/v${VERSION_SHAARLI}/shaarli-v${VERSION_SHAARLI}-full.tar.gz
\  
&& tar xzf shaarli-v${VERSION_SHAARLI}-full.tar.gz \  
&& mv /tmp/Shaarli /shaarli \  
&& wget https://github.com/kalvn/Shaarli-
Material/archive/v${VERSION_MATERIAL}.tar.gz \  
&& tar xzf v${VERSION_MATERIAL}.tar.gz \  
&& mv Shaarli-Material-${VERSION_MATERIAL}/material /shaarli/tpl/ \  
&& rm -rf v${VERSION_MATERIAL}.tar.gz Shaarli-Material-${VERSION_MATERIAL} \  
&& wget
https://github.com/ArthurHoaro/shaarli2twitter/archive/v${VERSION_SHAARLI2TWITTER}.tar.gz
\  
&& tar xzf v${VERSION_SHAARLI2TWITTER}.tar.gz \  
&& mv shaarli2twitter-${VERSION_SHAARLI2TWITTER}/shaarli2twitter
/shaarli/plugins/ \  
&& rm -rf v${VERSION_SHAARLI2TWITTER}.tar.gz
shaarli2twitter-${VERSION_SHAARLI2TWITTER} \  
&& cd /shaarli && chmod +w cache pagecache data tmp \  
&& rm -rf /tmp/* /var/cache/apk/* /usr/src/*  
  
COPY nginx/sites-enabled/shaarli.conf /nginx/sites-enabled/  
  
COPY nginx/conf.d/*.conf /nginx/conf.d/  
  
COPY startup /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/startup  
  
VOLUME /shaarli/data /shaarli/tpl /shaarli/plugins  
  
ENTRYPOINT ["/usr/local/bin/startup"]  
CMD ["/bin/s6-svscan", "/etc/s6.d"]  

