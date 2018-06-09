FROM alpine:edge  
  
MAINTAINER FEILLANT Thomas <thomas.feillant@biig.fr>  
  
RUN apk --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing add exim libcap  
  
RUN mkdir /etc/exim/conf.d /var/log/exim /usr/lib/exim /var/spool/exim \  
&& ln -s /dev/stdout /var/log/exim/main \  
&& ln -s /dev/stderr /var/log/exim/panic \  
&& ln -s /dev/stderr /var/log/exim/reject \  
&& chown -R exim: /var/log/exim /usr/lib/exim /var/spool/exim \  
&& chmod 0755 /usr/sbin/exim \  
&& setcap cap_net_bind_service=+ep /usr/sbin/exim \  
&& apk del libcap  
  
COPY exim.conf /etc/exim/  
COPY conf.d/* /etc/exim/conf.d/  
  
ENV EXIM_GMAIL_LOGIN= \  
EXIM_GMAIL_PASSWORD=  
ENV EXIM_RELAY_FROM_HOSTS=10.0.0.0/8:172.16.0.0/12:192.168.0.0/16  
USER exim  
EXPOSE 2525  
ENTRYPOINT ["/usr/sbin/exim"]  
  
CMD ["-bdf", "-q15m"]  

