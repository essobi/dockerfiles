FROM particlekit/ldap-client  
MAINTAINER TTP/ITP <admin@particle.kit.edu>  
  
RUN zypper --gpg-auto-import-keys --non-interactive ref && \  
zypper --gpg-auto-import-keys --non-interactive up && \  
zypper --gpg-auto-import-keys --non-interactive in -l \  
cups cups-filters cups-filters-cups-browsed poppler-tools \  
gutenprint OpenPrintingPPDs-ghostscript OpenPrintingPPDs \  
OpenPrintingPPDs-hpijs OpenPrintingPPDs-postscript hplip \  
hplip-hpijs hplip-sane manufacturer-PPDs gnu-free-fonts \  
hostname which bc && \  
zypper clean --all  
  
VOLUME ["/config", "/filter"]  
  
ENV CUPS_PASSWD=false \  
CUPS_LOGIN=root  
  
EXPOSE 631  
ADD init.sh /init-cups.sh  
CMD ["/init-cups.sh"]  

