FROM node:7-alpine  
MAINTAINER Tobias L. Maier <tobias.maier@baucloud.com>  
  
ARG
HUNSPELL_BASE_URL="http://download.services.openoffice.org/contrib/dictionaries"  
RUN npm install --save -g markdown-spellcheck  
  
COPY entrypoint.sh /  
  
RUN apk add --no-cache \  
hunspell  
  
RUN mkdir -p /tmp/hunspell /usr/share/hunspell \  
&& { \  
echo "2478723ab67dd801ec6add11b1af9d32665e7859a1cb00c95bfc2b618584a802
de_AT.zip"; \  
echo "c30bb085ba0a3d22a23aef51f4dd94ae9ae0cc811c0590ebf3713a93b209d823
de_CH.zip"; \  
echo "220e01c3137000305247336d8d10cd550bda3990fb10e50b31633947969a34b8
de_DE_comb.zip"; \  
echo "5ad7ce9710865c02e2b9e0790a48ca82ef6dd9e2537a19e8614fbc6a2ef6d2d4
de_DE_neu.zip"; \  
echo "22e217a631977d7b377f8dd22d2bbacd2d36b32765ce13f3474b03a4a97dd700
en_AU.zip"; \  
echo "31fac12a1b520cde686f328d3fa7560f6eba772cddc872197ff842c57a0dc1ea
en_CA.zip"; \  
echo "5869d8bd80eb2eb328ebe36b356348de4ae2acb1db6df39d1717d33f89f63728
en_GB.zip"; \  
echo "6cc717b4de43240595662a2deef5447b06062e82380f5647196f07c9089284fa
en_NZ.zip"; \  
echo "9227f658f182c9cece797352f041a888134765c11bffc91951c010a73187baea
en_US.zip"; \  
echo "090285b721dcaabff51b467123f82a181a6904d187c90bda812c6e5f365ff19a
en_ZA.zip"; \  
} > /tmp/hunspell-sha256sum.txt \  
&& cd /tmp/hunspell \  
&& for file in $(awk '{print $2}' /tmp/hunspell-sha256sum.txt); do \  
wget -O "${file}" "${HUNSPELL_BASE_URL}/${file}"; \  
grep "${file}" /tmp/hunspell-sha256sum.txt | sha256sum -c -; \  
unzip "/tmp/hunspell/${file}"; \  
done \  
&& cp *.aff *.dic /usr/share/hunspell \  
&& rm -rf /tmp/*  
  
WORKDIR /workdir  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["--help"]

