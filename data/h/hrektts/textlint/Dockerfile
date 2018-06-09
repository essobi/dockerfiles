FROM hrektts/ubuntu:latest  
LABEL maintainer="mps299792458@gmail.com" \  
version="9.1.1"  
  
ENV TEXTLINT_VERSION=9.1.1  
  
RUN wget -qO - https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g \  
textlint@${TEXTLINT_VERSION} \  
textlint-rule-preset-jtf-style \  
textlint-rule-ja-no-abusage \  
textlint-rule-ja-no-mixed-period \  
textlint-rule-ja-no-successive-word \  
textlint-rule-ja-no-weak-phrase \  
textlint-rule-max-comma \  
textlint-rule-max-kanji-continuous-len \  
textlint-rule-max-ten \  
textlint-rule-no-double-negative-ja \  
textlint-rule-no-doubled-conjunction \  
textlint-rule-no-doubled-conjunctive-particle-ga \  
textlint-rule-no-doubled-joshi \  
textlint-rule-no-dropping-the-ra \  
textlint-rule-no-exclamation-question-mark \  
textlint-rule-no-hankaku-kana \  
textlint-rule-no-mix-dearu-desumasu \  
textlint-rule-no-nfd \  
textlint-rule-sentence-length \  
textlint-rule-spellcheck-tech-word  
  
WORKDIR /data  
VOLUME ["/data"]  

