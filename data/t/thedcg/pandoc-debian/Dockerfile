################################  
# Dockerfile: thedcg/tl-debian:9  
  
# ベース  
FROM debian:9  
  
################################  
# Dockerfile.common  
  
# 管理者  
MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# Timezone  
ENV TZ=Asia/Tokyo  
  
# アップデート  
RUN date --iso-8601=ns\  
&& apt-get update\  
&& apt-get -y upgrade\  
&& DEBIAN_FRONTEND=noninteractive\  
apt-get -y install\  
tzdata\  
make\  
git\  
openssh-client\  
xz-utils\  
pandoc\  
pandoc-citeproc\  
tex-common\  
latex-cjk-all\  
texlive-generic-extra\  
texlive-lang-cjk\  
texlive-lang-polish\  
texlive-latex-extra\  
texlive-pictures\  
texlive-science\  
texlive-fonts-recommended\  
texlive-fonts-extra\  
texlive-metapost\  
texlive-bibtex-extra\  
texlive-publishers\  
biber\  
asymptote\  
gnuplot\  
poppler-utils\  
pngcheck\  
imagemagick\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*\  
&& echo "${TZ}" > /etc/timezone\  
&& ln -sf "/usr/share/zoneinfo/${TZ}" /etc/localtime\  
&& dpkg-reconfigure --frontend noninteractive tzdata\  
&& kanji-config-updmap-sys ipaex\  
&& date --iso-8601=ns  
  
# 終了  

