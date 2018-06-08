# yamkr-gitbook  
FROM billryan/gitbook:latest  
MAINTAINER JUN-HAN LIN (http://yamkr.com, john.lin@yamkr.com)  
  
ENV PATH /srv/dropbox_uploder/:$PATH  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends pdftk && \  
apt-get clean  
  
ADD fonts /usr/local/share/fonts/  
ADD dropbox_uploader.sh /srv/dropbox_uploder/  
  
RUN chmod +x /srv/dropbox_uploder/dropbox_uploader.sh && \  
fc-cache -v  
  
CMD ["gitbook", "--help"]

