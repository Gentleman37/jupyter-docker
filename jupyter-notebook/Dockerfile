FROM ubuntu:18.04
RUN apt-get update && apt-get -y update

RUN apt-get install -y build-essential python3.8 python3-pip python3-dev
RUN pip3 -q install pip --upgrade

WORKDIR /app

COPY ./src .
COPY ./requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install matplotlib seaborn

RUN pip3 install jupyter

RUN jupyter contrib nbextension install
RUN jupyter nbextensions_configurator enable --user
RUN jupyter nbextension enable toc2/main

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
