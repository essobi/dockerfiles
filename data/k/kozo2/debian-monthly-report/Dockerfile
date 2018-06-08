FROM debian:sid  
RUN sed -i -e "s/http.debian.net/dennou-k.gfd-dennou.org/g"
/etc/apt/sources.list; apt-get update; apt-get install -y ptex-bin okumura-
clsfiles texlive-latex-extra lv make git locales; echo "ja_JP.EUC-JP EUC-JP"
>> /etc/locale.gen; echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen; locale-gen;
git clone git://git.debian.org/git/tokyodebian/monthly-report.git; cd
/monthly-report; cp git-pre-commit.sh .git/hooks/pre-commit; make
debianmeetingresume201210-kansai.pdf  

