FROM debian:jessie  
  
COPY ./sources.list /etc/apt/sources.list  
  
RUN apt-get update \  
&& apt-get install -y curl apt-transport-https \  
&& curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - \  
&& echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list \  
&& apt-get update \  
&& apt-get install -y varnish \  
&& rm -rf /var/lib/apt/lists/*  
  
#RUN curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" \  
# && chmod +x /usr/local/bin/gosu  
ENV USER maxwin  
ENV GROUP maxwin  
ENV HOME /${USER}  
  
RUN groupadd -g 1000 ${USER} \  
&& useradd -u 1000 -g 1000 -c "${GROUP}" -d /${HOME} -s /bin/bash ${GROUP} \  
&& mkdir -p ${HOME} \  
&& chown -R ${USER}:${GROUP} ${HOME}  
  
WORKDIR ${HOME}  
  
COPY start.sh ${HOME}/start.sh  
COPY default.vcl /etc/varnish/default.vcl  
  
RUN chown ${USER}:${GROUP} ${HOME}/start.sh \  
&& chmod +x ${HOME}/start.sh \  
&& chown -R ${USER}:${USER} /etc/varnish/ \  
&& chown -R ${USER}:${USER} /var/lib/varnish/  
  
#USER ${USER}  
EXPOSE 80  
# Expose volumes to be able to use data containers  
VOLUME ["/var/lib/varnish", "/etc/varnish"]  
  
CMD ["./start.sh"]

