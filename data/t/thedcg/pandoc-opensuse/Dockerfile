################################  
# Dockerfile: thedcg/pandoc-opensuse:latest  
  
# ベース  
FROM opensuse:latest  
  
################################  
# Dockerfile.common  
  
# 管理者  
MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# アップデート  
RUN date --iso-8601=ns\  
&& zypper --non-interactive repos\  
&& zypper --non-interactive --gpg-auto-import-keys addrepo
http://download.opensuse.org/repositories/devel:languages:haskell/openSUSE_Leap_42.2/devel:languages:haskell.repo\  
&& zypper --non-interactive --gpg-auto-import-keys refresh\  
&& zypper --non-interactive --gpg-auto-import-keys update\  
&& zypper --non-interactive --gpg-auto-import-keys install\  
make\  
which\  
git\  
xz\  
tar\  
zip\  
texlive\  
texlive-asymptote\  
texlive-biblatex-science\  
texlive-cjk\  
texlive-cjk-latex-extras\  
texlive-cjkpunct\  
texlive-cjkutils\  
texlive-collection-basic\  
texlive-collection-bibtexextra\  
texlive-collection-binextra\  
texlive-collection-fontsextra\  
texlive-collection-fontsrecommended\  
texlive-collection-genericextra\  
texlive-collection-genericrecommended\  
texlive-collection-latexextra\  
texlive-collection-latexrecommended\  
texlive-collection-mathextra\  
texlive-collection-metapost\  
texlive-collection-pstricks\  
texlive-collection-publishers\  
texlive-collection-science\  
texlive-geometry\  
texlive-hyperref\  
texlive-japanese\  
texlive-japanese-otf-uptex\  
texlive-jsclasses\  
texlive-listings\  
texlive-pdfjam\  
texlive-ptex\  
texlive-ptex2pdf\  
texlive-pxcjkcat\  
texlive-pxjahyper\  
texlive-pxrubrica\  
texlive-setspace\  
texlive-uptex\  
ghostscript-cjk\  
perl-biber\  
pandoc\  
ghc-pandoc-citeproc\  
&& date --iso-8601=ns  
  
# 終了  

