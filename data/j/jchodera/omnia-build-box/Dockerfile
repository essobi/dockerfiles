FROM phusion/holy-build-box-64:1.2.0  
#  
# Install TeX  
#  
RUN yum clean -y --quiet expire-cache && \  
yum clean -y --quiet all  
  
# Make sure wget and zip installed  
RUN yum install -y --quiet wget zip  
  
# Install TeXLive  
ADD http://ctan.mackichan.com/systems/texlive/tlnet/install-tl-unx.tar.gz .  
ADD texlive.profile .  
RUN tar -xzf install-tl-unx.tar.gz && \  
cd install-tl-* && ./install-tl -profile /texlive.profile && cd \- && \  
rm -rf install-tl-unx.tar.gz install-tl-* texlive.profile && \  
/usr/local/texlive/2015/bin/x86_64-linux/tlmgr install \  
cmap fancybox titlesec framed fancyvrb threeparttable \  
mdwtools wrapfig parskip upquote float multirow hyphenat caption \  
xstring  
ENV PATH=/usr/local/texlive/2015/bin/x86_64-linux:$PATH  

