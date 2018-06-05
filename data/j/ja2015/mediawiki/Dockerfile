FROM mediawiki:latest  
# Enable mod_rewrite  
RUN a2enmod rewrite  
  
# Enable Lua  
ADD lua /usr/bin/  
RUN chmod 755 /usr/bin/lua  
  
# Extensions setup  
WORKDIR /var/www/html/extensions  
  
RUN git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/CategoryTree.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/CodeEditor.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/CodeMirror.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/GeoData.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/intersection.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/LabeledSectionTransclusion.git
\  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/MobileFrontend.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/PageImages.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Popups.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/RelatedArticles.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/Scribunto.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/TextExtracts.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/timeline.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/UserMerge.git \  
&& git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/extensions/VisualEditor.git \  
&& cd VisualEditor \  
&& git submodule update --init \  
&& cd lib/ve \  
&& rm -rf ./.git* ./LICENSE.txt ./README.md \  
&& cd /var/www/html/extensions \  
&& rm -rf ./*/.git* ./*/LICENSE.txt ./*/README.md  
  
  
# Skins setup  
WORKDIR /var/www/html/skins  
  
RUN git clone -b ${MEDIAWIKI_BRANCH}
https://gerrit.wikimedia.org/r/p/mediawiki/skins/MinervaNeue.git \  
&& rm -rf ./*/.git* ./*/LICENSE.txt ./*/README.md  
  
# Setup finish  
WORKDIR /var/www/html  

