FROM python:3.9.1

WORKDIR /home/sea_battle_app

RUN python -m pip install --upgrade pip

COPY sea_battle_app/requirements.txt /home/sea_battle_app/requirements.txt
RUN pip install -r requirements.txt

COPY sea_battle_app/ /home/sea_battle_app/