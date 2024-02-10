
FROM python:3.9-buster

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN apt install dos2unix
RUN apt-get install yasm libvpx. libx264. -y


RUN pip3 install -U pip
RUN pip3 install spleeter
RUN pip3 install typer


COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U -r requirements.txt
RUN mkdir /kony
WORKDIR /kony
COPY start.sh /start.sh

RUN dos2unix /start.sh
CMD ["/bin/bash", "/start.sh"]
