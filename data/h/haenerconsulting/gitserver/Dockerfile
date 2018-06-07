FROM alpine:latest  
  
EXPOSE 80  
VOLUME ["/git", "/var"]  
  
RUN apk add --no-cache \  
git-daemon \  
lighttpd \  
lighttpd-mod_auth  
  
COPY conf/* /etc/lighttpd/  
  
#RUN git config --global user.email "git@haenerconsulting.com" && \  
# git config --global user.name "git bot"  
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

