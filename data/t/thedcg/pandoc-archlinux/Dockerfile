################################  
# Dockerfile: thedcg/pandoc-archlinux:latest  
  
# ベース  
FROM pritunl/archlinux:latest  
  
################################  
# Dockerfile  
  
# 管理者  
MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# Timezone  
ENV TZ=Asia/Tokyo  
  
# アップデート  
RUN date --iso-8601=ns\  
&& pacman --sync --refresh --sysupgrade --noconfirm\  
core/tzdata\  
core/make\  
core/openssh\  
extra/git\  
extra/mesa-libgl\  
extra/texlive-bin\  
extra/texlive-core\  
extra/texlive-genericextra\  
extra/texlive-fontsextra\  
extra/texlive-langjapanese\  
extra/texlive-latexextra\  
extra/texlive-pictures\  
extra/texlive-science\  
extra/texlive-bibtexextra\  
extra/texlive-publishers\  
community/biber\  
extra/ghostscript\  
extra/poppler-data\  
extra/asymptote\  
community/pandoc\  
community/pandoc-citeproc\  
community/pandoc-crossref\  
&& echo "${TZ}" > /etc/timezone\  
&& ln -sf "/usr/share/zoneinfo/${TZ}" /etc/localtime\  
&& ln -s /usr/bin/vendor_perl/biber /usr/bin\  
&& kanji-config-updmap-sys ipaex\  
&& date --iso-8601=ns  
  
# 終了  

