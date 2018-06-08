FROM bcroq/stackless:2.7.9  
RUN set -x \  
&& easy_install --find-links=http://www.nagare.org/snapshots/ -Z
nagare.examples  
  
EXPOSE 8080  
ENTRYPOINT ["nagare-admin"]  
CMD ["serve", "--host", "0.0.0.0", "admin", "demo", "wiki", "gallery",
"portal", "jewels"]  

