FROM mayanedmsng/mayanedmsng:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#My custom additions  
RUN pip install datefinder  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libimage-exiftool-perl \  
python-regex \  
&& \  
apt-get clean autoclean && \  
apt-get autoremove --purge -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -f /var/cache/apt/archives/*.deb  
  
#COPY --from=nginx:latest  
RUN mkdir /srv/app_srcs  
COPY ./src/apps/document_analyzer /srv/app_srcs/document_analyzer  
RUN chown -R www-data:www-data /srv/app_srcs  
RUN ln -s /srv/app_srcs/document_analyzer/document_analyzer/
/usr/local/lib/python2.7/dist-packages/mayan/apps/document_analyzer  
  
# Retain the original entrypoint and command  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["mayan"]

