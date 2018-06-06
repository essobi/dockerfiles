FROM slitaz/slitaz-base:2.19  
RUN tazpkg recharge && \  
tazpkg -gi lighttpd && \  
tazpkg -cc  
  
COPY index.html /var/www/.  
  
EXPOSE 80  
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

