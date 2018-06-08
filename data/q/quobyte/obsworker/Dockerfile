FROM opensuse:13.2  
RUN zypper ar -n "openSUSE-13.2 OSS"
http://download.opensuse.org/distribution/13.2/repo/oss/ repo-13.2-oss  
RUN zypper --non-interactive --no-gpg-checks refresh; zypper --non-interactive
--no-gpg-checks install which aaa_base tar  
RUN zypper ar -f
http://download.opensuse.org/repositories/OBS:/Server:/2.6/openSUSE_13.2/ obs  
RUN zypper --non-interactive --no-gpg-checks refresh; zypper --non-interactive
--no-gpg-checks install obs-worker  
  
ADD ./main.sh /opt/main.sh  
ENTRYPOINT ["/opt/main.sh"]  

