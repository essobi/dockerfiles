# 必要ライブラリがインストール済のubuntu  
FROM korosuke613/all-in-ubuntu  
MAINTAINER Futa HIRAKOBA  
  
# 作業用フォルダの作成  
WORKDIR /home/  
RUN mkdir tmp  
WORKDIR /home/tmp  
  
# ToppersからMakefileをダウンロード、解凍  
RUN wget http://www.toppers.jp/download.cgi/ev3rt-beta7-1-release.zip  
RUN unzip ev3rt-beta7-1-release.zip  
  
# hrp2の解凍、移動  
RUN tar Jxvf ev3rt-beta7-1-release/hrp2.tar.xz  
RUN mv hrp2 /home/  
  
# cfgをmake  
WORKDIR /home/hrp2/cfg  
RUN make  
  
# 作業用ディレクトリの削除  
RUN rm -rf /home/tmp  
  
# makeのラッパースクリプトを追加  
ADD make_src.sh /home/hrp2/sdk/workspace  
  
# make_src.shを使用可能に  
WORKDIR /home/hrp2/sdk/workspace  
RUN chmod 755 make_src.sh  
CMD /home/hrp2/sdk/workspace/make_src.sh  
  

