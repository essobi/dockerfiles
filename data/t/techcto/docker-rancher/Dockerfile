#FROM rancher/server:preview  
FROM rancher/server:latest  
  
ENV
DEFAULT_CATTLE_CATALOG_URL='{"catalogs":{"solodev":{"url":"https://github.com/techcto/datacenter.git"}}}'  
# ENV CATTLE_UI.PL='Solodev Datacenter'  
# COPY logos /usr/share/cattle/war/assets/images/logos  
ENTRYPOINT ["/usr/bin/entry"]  
CMD ["/usr/bin/s6-svscan", "/service"]

